from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView, name='home'),
    path('drinks/',views.DrinkList, name='drinks'),
    path('drink-details/<str:pk>',views.DrinkDetails, name='drink-details'),
    path('create-drink/',views.createDrink, name='create-drink'),
    path('update-drink/<str:pk>', views.updateDrink, name='update-drink'),
    path('delete-drink/<str:pk>', views.deleteDrink, name='delete-drink')
]
