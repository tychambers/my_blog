from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'home.html', {'posts': posts})

def about(request):
	context = {
	"variable1":[0,1,2,3,4,5,6],
	"variable2": "Hello All!"
	}
	return render(request, 'about.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})