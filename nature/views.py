from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')



class PostList(ListView):
    model = Post
    template_name = 'index.html'  # Använd korrekt sökväg för templates
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


class PostDetailView(DetailView):
    model = Post
    template_name = 'nature/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context


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
