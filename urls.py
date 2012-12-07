from django.conf.urls.defaults import *
from django.views.generic import list_detail
from python.views import hello, current_datetime, hours_ahead
from django.contrib import admin
from python.library import views
from python.library.models import Book
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

book_info = {
    'queryset': Book.objects.all(),
    'template_name': 'book_list_page.html',
}

urlpatterns = patterns('',
        (r'^books/$', list_detail.object_list, book_info),
        (r'^search/$', views.search),
        (r'^search-form/$', views.search_form),
	('^hello/$', hello),
	('^time/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
        (r'^admin/', include(admin.site.urls)),
)
