from django.urls import path
from . import views #in reference to the other file in our folder

urlpatterns = [
     path('',views.home, name='home'),    #this is the 1st to add
     
     path('register/',views.registerPage, name='register'),
     path('login/',views.loginPage, name='login'),
     path('logout/',views.logoutUser, name='logout'),

     path('user/', views.userPage, name='user-page'),
     path('qr/<str:pk>/',views.qr, name='qr'),
     path('crear_qr/<str:pk>/', views.crearQr, name='crear_qr'),
     path('update_qr/<str:pk>', views.updateQr, name='update_qr'),
     path('delete_qr/<str:pk>', views.deleteQr, name='delete_qr')
]