from django.urls import reverse
from operator import truediv
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank='true', null='true')
    created_on = models.DateTimeField(auto_now_add=True)
    meta_description = models.CharField(max_length=160, unique=True, null='true')
    #cover_image = models.ImageField(null='true',blank='true', upload_to='thumbnails/')
    #thumb = ImageSpecField(source = 'cover_image', processors = [SmartResize(250,150)], format='PNG')
    #cover_image_alt = models.CharField(max_length=200, default = 'STRING')
    image = models.ImageField(null='true',blank='true', upload_to='images/')
    smart = ImageSpecField(source = 'image', processors = [SmartResize(500,300)], format='PNG')
    image_alt = models.CharField(max_length=200, default = 'STRING')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])