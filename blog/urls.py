from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^$', TemplateView.as_view(template_name="blog/home.html"), name="home"),
	url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="user-logout"),
	url(r'^post/$', views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
	url(r'post/new/$', views.post_new, name = 'post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),
	url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name = 'post_delete'),
	url('', include('social.apps.django_app.urls', namespace='social')),
]