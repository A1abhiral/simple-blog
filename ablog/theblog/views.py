from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from theblog.models import Post,Category
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.\
#def home(request):
 #   return render(request,'home.html',{})

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)
        
    
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

def CategoryView(request,cat):
    category_post = Post.objects.filter(category=cat.replace('-',' '))
    cat_menu = Category.objects.all()
    return render(request,'categories.html',{'cat':cat.replace('-',' '),'category_post':category_post,'cat_menu':cat_menu})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"]=liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "Update_post.html"
    #fields = ('title','body')

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = "Delete_post.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

    