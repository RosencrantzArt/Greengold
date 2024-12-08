from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator  # To use decorators on class-based views
from django.contrib.auth.decorators import user_passes_test  # To restrict access to admin views
from .models import Post, Comment
from django import forms
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

# Define admin_only function to restrict access to admin users
def admin_only(user):
    return user.is_superuser

# Comment form (defined here as you're not using forms.py)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }

# Function to add a comment
@login_required
def add_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        
        # Check if the form is valid
        if comment_form.is_valid():
            # Create and save the comment, linking it to the user and the post
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Link the comment to the logged-in user
            comment.save()

            # Feedback to the user
            messages.success(request, "Your comment has been posted successfully!")

            # Redirect back to the post detail page after the comment is created
            return redirect('post_detail', slug=post_slug)

        else:
            # If the comment is invalid, send an error message
            messages.error(request, "Comment cannot be empty. Please write something.")

    else:
        # If it's not a POST request, create an empty form
        comment_form = CommentForm()

    # Render the post detail page with the comment form
    return render(request, 'nature/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
    })

# Function to delete a comment
@login_required
def delete_comment(request, post_slug, comment_id):
    # Get the specific post by slug
    post = get_object_or_404(Post, slug=post_slug)
    
    # Get the comment by ID and ensure it belongs to the post
    comment = get_object_or_404(Comment, id=comment_id, post=post)
    
    # Ensure that the logged-in user is the author of the comment
    if comment.author != request.user:
        raise Http404("You are not allowed to delete this comment.")

    # Delete the comment
    comment.delete()

    # Provide feedback to the user
    messages.success(request, "Your comment has been deleted.")

    # Redirect back to the post detail page
    return redirect('post_detail', slug=post_slug)


# List all posts
class PostList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_at')

# Show a specific post
class PostDetailView(DetailView):
    model = Post
    template_name = 'nature/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

# Create a new post (Admin only)
@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'nature/post_create.html'
    fields = ['title', 'content', 'status', 'slug']
    success_url = reverse_lazy('home') 

# Update a post (Admin only)
@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'nature/post_update.html'
    fields = ['title', 'content', 'status', 'slug']
    success_url = reverse_lazy('home')

# Delete a post (Admin only)
@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'nature/post_confirm_delete.html'
    success_url = reverse_lazy('home')

# User registration function
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created, login.")
            return redirect('login')
        else:
            messages.error(request, "Error, make sure you have filled in the forms correctly.")
    else:
        form = UserCreationForm()

    return render(request, 'nature/register.html', {'form': form})

# About page function
def about(request):
    return render(request, 'about.html')

# Custom logout message (clearing old messages and adding a new one)
@receiver(user_logged_out)
def custom_logout_message(sender, request, **kwargs):
    # Clear all previous messages before adding a new one
    messages.get_messages(request).used = True
    
    if request.user.is_authenticated:  # Ensure the user is logged in before adding the message
        # Add a custom logout message
        messages.success(request, f"Thank you {request.user.username}, hope to see you again!")
