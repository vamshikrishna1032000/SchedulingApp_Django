from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="index"),
    path('index', views.user_login, name="index"),
    path('login', views.user_login, name="login.html"),
    path('home' ,  views.user_home, name='home'),
    path('logout', views.user_logout, name="logout"),
    path('register', views.register, name="register.html"),
    path('forgotpasw', views.forgotpasw, name="forgotpasw.html"),
    path('addsession', views.addsession, name="newsession"),
    path('availability', views.availability, name="availability"),
    path('check_avail',views.check_avail, name="checking_availability"),
    path('add_assignment', views.add_assignment, name="add_assignment"),
    path('test', views.test, name="testing"),
    path('testdash', views.testdash, name="testingdashboard"),
]