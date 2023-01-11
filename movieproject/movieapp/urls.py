from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movi_id>/',views.details,name='details'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]