from django.urls import path
from .views import CreatePostView, GetPostsView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('all/', GetPostsView.as_view(), name='get_posts'),
]
