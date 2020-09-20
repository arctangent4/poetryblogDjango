from .models import Issue

def blog_menu(request):

    issue_menu = Issue.objects.all()
    return {
        'issue_menu': issue_menu
    }