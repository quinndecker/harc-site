from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'home.html')
#def aboutus(request):
    #return render(request, 'tabs/about-us.html')
def servicearea(request):
    return render(request, 'tabs/service-area.html')
    
#ContactForm#
def contactus(request):
    context={'form': ContactForm()}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Area Rug Cleaning Request"
            body = {
                'firstName': form.cleaned_data['firstName'],
                'lastName' : form.cleaned_data['lastName'],
                'emailAddress': form.cleaned_data['emailAddress'],
                'phoneNumber' : form.cleaned_data['phoneNumber'],
                'address1' : form.cleaned_data['address1'],
                'city' : form.cleaned_data['city'],
                'state' : form.cleaned_data['state'],
                'zipCode' : form.cleaned_data['zipCode'],
                'message' : form.cleaned_data['message'],
                'serviceDate': form.cleaned_data['serviceDate'],
            }
            name = "Name:"+' '+ body.get('firstName')+" "+body.get('lastName')+'\n'
            email = "Email:"+' '+body.get('emailAddress')+'\n'
            phone = "Phone Number:"+' '+body.get('phoneNumber')+'\n'
            address = "Address:"+' '+body.get('address1')+' '+body.get('city')+","+" "+ body.get('state')+' '+body.get('zipCode')+'\n'
            msg = "Message:"+' '+body.get('message')+'\n'
            appt = "Desired Pickup Date/Time:"+' '+body.get('serviceDate')

            message = f"{name}\n{email}\n{phone}\n{address}\n{msg}\n{appt}"
            try:
                send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.RECIPIENT_ADDRESS])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            return redirect('contact-success/')
    form = ContactForm()
    return render(request, 'tabs/contact-us.html',context)

def contactsuccess(request):
    return render(request, 'contact-success.html')

    #when booking app is completed
#def booking(request):
#    return render(request, 'booking-templates/book-now.html')

## Blog Stuff ##

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

#info for sitemap#
def Post(request, post_slug=Post.slug):

    item = get_object_or_404(Post, slug=post_slug)

    return render(request,'post_detail.html', {'post': item})
