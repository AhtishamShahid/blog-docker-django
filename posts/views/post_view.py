from django.shortcuts import render
from django.views import generic
from ..models import Post, Comments, Category
from django.http import HttpResponse


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = '4'

    def get_queryset(self):
        print(self.request.user.is_authenticated, 'user')
        category = self.request.GET.get('category', None)
        if category is None:
            return Post.objects.all()
        else:
            return Post.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/blog-single.html'


def test(request, post_id):
    data = Post.objects.get(id=1).category.all()
    print(data)
    # cat = data.category.all()
    return HttpResponse(data)
