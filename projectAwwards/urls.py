from django.urls import path, include
from . import views
from projectAwwards import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name = 'index'),
    path('accounts/signUp/', views.signUp, name='signUp'),
    # path('account/', include('django.contrib.auth.urls')),
    path('userProfile/', views.userProfile,name = 'userProfile'),
    path('update_profile/', user_views.update_profile,name = 'update_profile'),
    path('search/', views.search_results, name = 'search_results'),
    path('post_project/', views.post_project,name ='post_project'),
    path(r'api/merch/', views.MerchList.as_view()),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

]

# if settings.DEBUG:
#    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

