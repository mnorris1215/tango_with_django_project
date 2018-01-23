from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

##class MyRegistrationView(RegistrationView):
##    def get_success_url(self, request, user):
##        return '/rango/'




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
##    url(r'^accounts/register/$', MyRegistrationView.as_view(),
##        name='registration_register'),
##    url(r'^accounts/', include('registration.urls')),
)

if settings.DEBUG:
# if DEBUG=TRUE, additional URL matching pattern is appended
# to the urlpatterns tuple
    urlpatterns += patterns(
        # This view handles the dispatching of uploaded media files 
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
