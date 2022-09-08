from django.urls import path
#now import the views.py file into this code
from . import views
#urlpatterns=[
#  path('',views.index)

#]

 
# importing views from views..py
from .views import home_view
 
urlpatterns = [
    path('', home_view ),
]