#from rest_framework import routers
from .views import getNotifyShopsView,updateBudgetChange
from django.urls import path
from django.conf.urls import include


urlpatterns = [
     path('NotifyShopsView/', getNotifyShopsView,name="NotifyShopsView"),
     path('updateBudgetChange/', updateBudgetChange,name="updateBudgetChange"),
]