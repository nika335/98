
from django.contrib import admin
from django.urls import path
from shearing_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('texts', views.texts),
    path('url/<str:urls>', views.urls, name='url'),
    path('edit/<str:urls>', views.edit_text, name='edit')
]
