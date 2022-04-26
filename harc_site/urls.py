from django.urls import path 
from . import views
from django.contrib import admin
admin.autodiscover()
from . import views




urlpatterns = [
    path('', views.index, name='homepage'),
    path('book-now/', views.booknow, name='booknow'),

     ## THIS HAS TO BE LAST##
    #-Blog Functionality-#
    path('admin/', admin.site.urls),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    ##THIS HAS TO BE LAST##
]