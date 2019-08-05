from django.urls import path

from .views import post_view, comment_view

app_name = 'posts'

urlpatterns = [
    path('', post_view.IndexView.as_view(), name='index'),
    path('<int:pk>/', post_view.DetailView.as_view(), name='detail'),
    path('<int:post_id>/test/', post_view.test, name='results'),
    path('<int:post_id>/comment', comment_view.comment, name='comment')
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
