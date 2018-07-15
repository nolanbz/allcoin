from django.conf.urls import url

from .views import (
	PostDetailView,
    PostCreateView,
    PostUpdateView,
)

urlpatterns = [
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),    
]