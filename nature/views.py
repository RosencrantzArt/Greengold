from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def admin_only(user):
    return user.is_superuser  



def about(request):
    return render(request, 'about.html')



class PostList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'nature/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        # Lägg till logik för likes/kommentarer om det behövs
        return context


@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'nature/post_create.html'
    fields = ['title', 'content', 'status', 'slug']
    success_url = reverse_lazy('home') 



@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'nature/post_update.html'
    fields = ['title', 'content', 'status', 'slug']
    success_url = reverse_lazy('home')



@method_decorator([login_required, user_passes_test(admin_only)], name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'nature/post_confirm_delete.html'
    success_url = reverse_lazy('home')


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
