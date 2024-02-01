from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    #class urls
    path('classhome',views.Tasklistview.as_view(),name='Tasklistview'),
    path('classdetail/<int:pk>/',views.Taskdetailview.as_view(),name='Taskdetailview'),
    path('classupdate/<int:pk>/',views.Taskupdateview.as_view(),name='Taskupdateview'),
    path('classdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='Taskdeleteview'),

]