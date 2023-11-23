from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path('mycontacts/', include('mycontacts.urls')),
    path('admin/', admin.site.urls),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'), 
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]