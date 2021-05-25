from django.urls import path,include
from django.contrib import admin
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views 
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('logout/', LogoutView.as_view(), {"next_page": '/'}), 
    path('api-token-auth/', obtain_auth_token)
]
