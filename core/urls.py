from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^$", "core._delete_me.demo_view", name="delete_me"),
    url(r"^demo/(?P<num>\d+)/$", "core._delete_me.demo_ajax", name="demo_ajax")
)

if settings.DEBUG:
    urlpatterns += patterns(
        "",
        (r"^media/(?P<path>.*)$",
         "django.views.static.serve",
         {"document_root": settings.MEDIA_ROOT}),
    )
