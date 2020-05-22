
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

from articles import views as article_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^about/$',views.about),


    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls')),

    url(r'^$', article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
