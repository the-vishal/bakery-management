from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^login/', views.upload_to_database),

    url(r'^order/', views.OrderManagerView.as_view(), name='place_order'),
    url(r'^history/', views.OrderManagerView.as_view()),
    url(r'^list/', views.ItemManagerView.as_view(), name='list_orders'),

    url(r'^item/', views.ItemManagerView.as_view(), name='item_management'),
    url(r'^ingredient/', views.IngredientManagerView.as_view(), name='manage_ingredient'),
]