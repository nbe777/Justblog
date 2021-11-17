from django.urls import path
from . import views

urlpatterns = [
    path('myprofile',views.myprofile,name='myprofile'),
    path('', views.home, name='home'),
    path('addblog/', views.addblog, name='addblog'),
    path('blogdetails/<int:pk>',views.blogdetails,name='blogdetails'),
    path('blogdetails/<int:pk>/profile',views.profile, name='profile'),
    path('addblog/seelistblog',views.seelistblog, name='seelistblog'),
    path('addblog/seelistblog/<int:pk>/update',views.update,name="update"),
    path('addblog/seelistblog/<int:pk>/delete',views.delete,name="delete"),

]
