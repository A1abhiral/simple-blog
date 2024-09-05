
from django.urls import path
from theblog.views import HomeView,ArticleDetail,AddPostView

urlpatterns = [
   #path('',views.home, name = "home")
   path('',HomeView.as_view(), name="home"),
   path('article/<int:pk>',ArticleDetail.as_view(),name ="article-detail"),
   path('add_post/',AddPostView.as_view(),name="add_post")
    

]
