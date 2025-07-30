from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Post

@method_decorator(csrf_exempt, name='dispatch')
class CreatePostView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            print("------------------------>", data)
            post = Post.objects.create(
                title=data.get('title'),
                content=data.get('content'),
                author=data.get('author'),
                published=data.get('published', False)
            )
            return JsonResponse({'message': 'Post created', 'id': post.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class GetPostsView(View):
    def get(self, request):
        posts = Post.objects.all().values()
        return JsonResponse({'posts': list(posts)}, status=200)
