from django.urls import path

from .import views
urlpatterns=[
    path('',views.index,name='home'),

    path('about/',views.about,name='about'),

    path('features/',views.features,name='features'),

    path('contact/',views.contact_view,name='contact')
]