from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('python',views.python,name='python'),
    path('getpycode/<int:id>', views.getpycode, name='getpycode'),
    
    ]
