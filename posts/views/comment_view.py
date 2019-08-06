"""
Comment
"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# from django.views import generic
from ..models import Comments, Post


def comment(request, post_id):
    """Comment handler"""
    try:
        post = get_object_or_404(Post, pk=post_id)
    except (KeyError, Post.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'post': post,
            'error_message': "You didn't select a choice.",
        })
    else:
        Comments.objects.create(text=request.POST.get('text'), post_id=post_id)
        return HttpResponseRedirect(reverse('posts:detail', args=(post_id,)))
