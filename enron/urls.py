from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('summery/', views.summery, name='summery'),
    path('<emailId>/emaildetails', views.emailcontent, name='emailcontent'),
    path('<staff_from>/<staff_to>/detail', views.mail_history, name='staffdetail'),
    path('staff/', views.staff, name='staff'),
]