from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('alltrainee', views.allTrainee, name='allTrainee'),
    path('update/<int:id>', views.updateTrainee, name='updateTrainee'),
    path('delete/<int:id>', views.deleteTrainee, name='deleteTrainee'),
    path('logout', views.logout, name="logout")
]
