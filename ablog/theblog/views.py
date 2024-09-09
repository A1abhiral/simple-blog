from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from theblog.models import Post,Category
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy

# Create your views here.\
#def home(request):
 #   return render(request,'home.html',{})
def CategoryView(request,cat):
    category_post = Post.objects.filter(category=cat.replace('-',' '))
    return render(request,'categories.html',{'cat':cat.replace('-',' '),'category_post':category_post})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "Update_post.html"
    #fields = ('title','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = "Delete_post.html"
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    