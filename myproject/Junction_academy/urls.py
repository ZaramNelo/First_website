from django.urls import path
from . import views

urlpatterns = [
    path("",views.Homepage, name="Homepage"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("Log_in",views.Log_in, name="Log_in"),
    path("free_trial",views.free_trial, name="free_trial"),
    path("profile",views.profile, name="profile"),
    path("Logout",views.Logout, name="Logout")
]