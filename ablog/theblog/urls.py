
from django.urls import path
from theblog.views import HomeView,ArticleDetail,AddPostView,UpdatePostView

urlpatterns = [
   #path('',views.home, name = "home")
   path('',HomeView.as_view(), name="home"),
   path('article/<int:pk>',ArticleDetail.as_view(),name ="article-detail"),
   path('add_post/',AddPostView.as_view(),name="add_post"),
   path('update_post/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    

]
