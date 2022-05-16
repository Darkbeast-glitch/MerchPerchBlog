from django.shortcuts import render
from .models import Post, AboutUs
from django.views import generic
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    post = Post.objects.all()
    aboutus = AboutUs.objects.all()
    paginator = Paginator(object_list, 5)  # 5 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list, 'post': post, 'aboutus': aboutus})




def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})







def Privacy_Policy(request):
    context = {}
    return render (request, 'privacy_policy.html', context)

    #aboutme

def AboutMe(request):
    context = {}
    return render (request, 'aboutme.html',context)

def Contact(request):
    context = {}

    return render(request, 'contact.html', context)



def page_not_found_view(request,exception):
    return render (request, '404.html', status=404)


def Crypto_stacks(request):
    return render (request, 'index_crypto.html')

def Simlock(request):
    return render (request, 'index_simlock.html')