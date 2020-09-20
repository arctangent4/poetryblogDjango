from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Issue
from .forms import PostForm, EditForm, IssueForm, IssueEditForm
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse

#def home(request):
    #return render(request, 'home.html',{})

# Create your views here.

class HomeView(ListView):
    model = Issue
    template_name = "home.html"
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
 
    
    
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name= 'add_post.html'
    #fields = "__all__"
    #fields = ('title', 'body')
    
class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    #fields = ['title', 'tab_title','author','body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
class IssueView(ListView):
    model = Issue
    template_name='issues.html'
    
def about_view(request):
    return render(request, 'about.html')

def submit_view(request):
    return render(request, 'submit.html')


#def issues_view(request):
#    return render(request, 'issues.html')

class EditIssueView(UpdateView):
    model = Issue
    form_class = IssueEditForm
    template_name= 'edit_issue.html'
    #fields = "__all__"
    #fields = ('title', 'body')
    
class AddIssueView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name= 'create_issue.html'
    #fields = "__all__"
    #fields = ('title', 'body')
    
class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_details.html'

    
    def get_context_data(self, **kwargs):
        context = super(IssueDetailView,self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    
def get_latest_issue(request): 
     issue = Issue.objects.latest('id')
     return HttpResponseRedirect(reverse('issue-detail', args=[issue.pk]))





    

    
