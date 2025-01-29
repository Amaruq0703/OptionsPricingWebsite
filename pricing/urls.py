from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("blackscholes", views.bsm, name='bsm'),
    path('binomial', views.bino, name='bino'),
    path('savecalculation/', views.save_calc, name='save'),
    path('saved', views.saved, name='saved'),
    path('savedcalculation/<int:calcID>', views.savedToModel, name='tomodel')
]