from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator  # För att använda decorators på klassmetoder
from django.contrib.auth.decorators import user_passes_test  # Lägg till denna import
from .models import Post, Comment
from django import forms

# Definiera admin_only funktionen före användning
def admin_only(user):
    return user.is_superuser

# Kommentarformulär (definieras här eftersom du inte använder forms.py)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }

# Funktion för att lägga till kommentarer
@login_required
def add_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        
        # Kontrollera om formuläret är giltigt
        if comment_form.is_valid():
            # Skapa och spara kommentaren, koppla den till användaren och posten
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Koppla kommentaren till den inloggade användaren
            comment.save()

            # Feedback till användaren
            messages.success(request, "Your comment has been posted successfully!")

            # Omdirigera tillbaka till postens detaljsida efter att kommentaren skapats
            return redirect('post_detail', slug=post_slug)

        else:
            # Om kommentaren inte är giltig, skicka meddelande om att kommentaren inte kan postas
            messages.error(request, "Comment cannot be empty. Please write something.")

    else:
        # Om det inte är en POST-förfrågan, skapa ett tomt formulär
        comment_form = CommentForm()

    # Rendera detaljsidan med kommentarformuläret
    return render(request, 'nature/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
    })

# Funktion för att gilla ett inlägg
@login_required
def like_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.user not in post.likes.all():
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)

    return JsonResponse({'likes': post.total_likes()})

# Lista alla inlägg
class PostList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_at')

# Visa ett specifikt inlägg
class PostDetailView(DetailView):
    model = Post
    template_name = 'nature/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

# Skapa nytt inlägg (Endast admin)
@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'nature/post_create.html'
    fields = ['title', 'content', 'status', 'slug']
    success_url = reverse_lazy('home') 

# Uppdatera ett inlägg (Endast admin)
@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'nature/post_update.html'
    fields = ['title', 'content', 'status', 'slug']
    success_url = reverse_lazy('home')

# Ta bort ett inlägg (Endast admin)
@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'nature/post_confirm_delete.html'
    success_url = reverse_lazy('home')

# Användarfunktioner
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

# Om-sida
def about(request):
    return render(request, 'about.html')
