from django.urls import path
from . import views

app_name='tweetapp'

urlpatterns = [
    path('', views.listtweet,name="listtweet"), #port/tweetapp/
    path('addtweet/',views.addtweet,name="addtweet"),#port/tweetapp/addtweet
    path('addtweetbyform/',views.addtweetbyform,name="addtweetbyform"),
    path('addtweetbymodelform/',views.addtweetbymodelform,name="addtweetbymodelform")
]
