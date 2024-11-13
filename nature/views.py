from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'nature/post_list.html'  
    context_object_name = 'post_list'  
    paginate_by = 10  

    def get_queryset(self):
        return Post.objects.filter(status=1)

class PostDetailView(DetailView):
    model = Post
    template_name = 'nature/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context


