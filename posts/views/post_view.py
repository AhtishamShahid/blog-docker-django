# from django.shortcuts import render
"""Create your views here."""
from django.views import generic
from django.http import HttpResponse
from ..models import Post, Category


# Create your views here.

class IndexView(generic.ListView):  # pylint: disable=too-many-ancestors
    """Index view class"""

    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = '4'

    def get_queryset(self):
        """get_queryset"""
        # print(self.request.user.is_authenticated, 'user')
        category = self.request.GET.get('category', None)
        data = []
        if category is None:
            data = Post.objects.all()
        else:
            data = Post.objects.filter(category=category)
        return data

    # def get_context_data(self, **kwargs):
    def get_context_data(self, *, object_list=None, **kwargs):
        """get_context_data"""
        context = super(IndexView, self).get_context_data(**kwargs, object_list=object_list)
        context['categories'] = Category.objects.all()
        return context


class DetailView(generic.DetailView):  # pylint: disable=too-many-ancestors
    """DetailView"""
    model = Post
    template_name = 'posts/blog-single.html'


def test(request, post_id):
    """test"""

    data = Post.objects.get(id=1).category.all()
    print(data)
    # cat = data.category.all()
    return HttpResponse(data)
