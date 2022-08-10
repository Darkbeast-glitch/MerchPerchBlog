from django.shortcuts import render
from .models import Post, AboutUs,ContactUs
from django.views import generic
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages


# Create your views here.


def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    post = Post.objects.all()
    aboutus = AboutUs.objects.all()
    paginator = Paginator(object_list, 6)  # 5 posts in each page
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
                  'frontpagenew.html',
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
    contact_us = ContactUs.objects.all()
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['surname']
        email = request.POST['email']
        needs = request.POST['need']
        de_message = request.POST['message']


        contact_form = ContactUs(firstname=firstname,lastname=lastname,email=email,forms_need=needs, de_message=de_message)
        contact_form.save()
        messages.success(request,"Your messages has been sent successfully our representative will reach out to you in a short time 😎")


    context={
        'contact_us':contact_us
    }
    return render(request, 'contact.html', context)



def page_not_found_view(request,exception):
    return render (request, '404.html', status=404)


def Crypto_stacks(request):
    return render (request, 'index_crypto.html')

def Simlock(request):
    return render (request, 'index_simlock.html')


def GiftCardHome(request):
    return render (request, 'gitcards.html')

def AmazonCard(request):
    return render (request, 'amazon.html')


def EbayCard(request):
    return render (request, 'ebay.html')


def Facebook(request):
    return render (request, 'facebook.html')

def Googleplay(request):
    return render (request, 'googleplay.html')


def Itunes(request):
    return render (request, 'itunes.html')


def Playstation(request):
    return render (request, 'playstation.html')

def Steam(request):
    return render (request, 'steam.html')

def Xbox(request):
    return render (request, 'xbox.html')


def Button(request):
    return render (request, 'button.html')


def CheckMe(request):
    return render(request, 'checkme.html',)

