from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.forms import UserCreationForm


class PostList(ListView):
    model = Post
    template_name = 'nature/post_list.html'  
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
            messages.success(request, "Ditt konto har skapats! Du kan nu logga in.")
            return redirect('login') 
        else:
            messages.error(request, "Ett fel uppstod. Kontrollera att alla fält är ifyllda korrekt.")
    else:
        form = UserCreationForm()  

    return render(request, 'nature/register.html', {'form': form})