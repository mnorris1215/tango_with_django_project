#This code imports the relevant Django machinery that we use
#to create URL mappings.
from django.conf.urls import patterns, url


#Importing the views module from rango also provides us with access
#to our simple view implemented previously, allowing us to reference
#the view in the URL mapping we will create.
from rango import views

#To create our mappings, we use a tuple.
#For Django to pick your mappings up,
#this tuple must be called urlpatterns.


#The first parameter we provide to the django.conf.urls.url() function
#is the regular expression ^$, which matches to an empty string.

#Any URL supplied by the user that matches this pattern means
#that the view views.index() would be invoked by Django.
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name ='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
            )




