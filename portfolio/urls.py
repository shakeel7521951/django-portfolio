from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio , name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout_view, name='logout'),
    path('', include('social_django.urls', namespace='social')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
