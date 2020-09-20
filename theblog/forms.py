from django import forms
from .models import Post,Issue

issue_colors =[('white','white'),('black','black'),('gray','gray')]

issue_titles = Issue.objects.all().values_list('name','name')
issue_list = []

for item in issue_titles:
    issue_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('issue_title','title','tab_title','author','body')
        
        widgets = {
            'issue_title': forms.Select(choices=issue_list,attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tab_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('issue_title','title','tab_title', 'author','body')
        
        widgets = {
            'issue_title': forms.Select(choices=issue_list,attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tab_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
           # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields =('name','title','parallaximage','color')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(choices=issue_colors,attrs={'class': 'form-control'}),

           # 'author': forms.Select(attrs={'class': 'form-control'}),

        }
        

        
class IssueEditForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields =('name','title','parallaximage','color')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(choices=issue_colors,attrs={'class': 'form-control'}),

           # 'author': forms.Select(attrs={'class': 'form-control'}),

        }