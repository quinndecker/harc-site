from django.urls import path 
from . import views
from django.contrib import admin
admin.autodiscover()
from . import views




urlpatterns = [
    path('', views.index, name='homepage'),
    path('booking/', views.booking, name='booking'),


     ## THIS HAS TO BE LAST##
    #-Blog Functionality-#
    path('admin/', admin.site.urls),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    ##THIS HAS TO BE LAST##
]