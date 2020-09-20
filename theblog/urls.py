from django.urls import path
from .models import Post, Issue
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView,EditPostView, DeletePostView,about_view, submit_view,IssueView, AddIssueView, IssueDetailView, EditIssueView, get_latest_issue
urlpatterns = [
    #path('', views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), path('add_post/', AddPostView.as_view(), name='add_post'), path('article/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('about/',about_view, name="about" ), path('submit/',submit_view, name="submit"), path('issue/',IssueView.as_view(), name="issue"),path('create_issue/',AddIssueView.as_view(), name="create_issue"),path('issue/<int:pk>', IssueDetailView.as_view(), name='issue-detail'),path('issue/edit/<int:pk>', EditIssueView.as_view(), name="edit_issue"), path('latest-issue/', get_latest_issue, name='latest-issue')

    
]





#path('latest-issue', latest-issue.redirector, name="latest-issue"),