from django.urls import path
from . import views
from projectAwwards import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/signUp/', views.signUp, name='signUp'),
]

if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
