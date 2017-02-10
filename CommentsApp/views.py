from django.shortcuts import render
from datetime import datetime

from . import models
from . import forms

# Create your views here.
def getComments(request):
    comments_list = models.Comment.objects.filter(parent=None)
    context = {
        'comments' : comments_list,
    }
    return render(request, 'comments.html', context)

def getCommentForm(request):
    return render(request, 'commentForm.html')

def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'], parent=None, time=datetime.now())
            new_comment.save()
            comments_list = models.Comment.objects.filter(parent=None)
            context = {
                'comments' : comments_list
            }
            return render(request, 'commentFormSuccess.html', context)
    else:
        form = forms.CommentForm()
    return render(request, 'commentForm.html')

def addReply(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        parent_comment_id = request.GET.get('id', 'None')
        parent = models.Comment.objects.get(id__exact=parent_comment_id)
        
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'], parent=parent)
            new_comment.time = datetime.now()
            new_comment.save()

            #parent.children.add(new_comment)
            #parent.save()
            parent.children_comment.add(new_comment)
            parent.save()

            comments_list = models.Comment.objects.filter(parent=None)
            context = {
                'comments' : comments_list
            }
            return render(request, 'commentFormSuccess.html', context)
    else:
        form = forms.CommentForm()
    return render(request, 'comments.html')