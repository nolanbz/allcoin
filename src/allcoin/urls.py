from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from posts.views import ListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ListView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^terms/$', TemplateView.as_view(template_name="terms.html"), name='terms'),
    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name='privacy'),    
    url(r'^', include('posts.urls', namespace='posts')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
