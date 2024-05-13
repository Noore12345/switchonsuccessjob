from django.urls import path
from . import views
urlpatterns=[
    path('register-recruiter/',views.register_recruiter, name='register-recruiter'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout')

]
