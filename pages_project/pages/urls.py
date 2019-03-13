from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), #as_view is a HomePageView class method that takes a request and reutrns a response
    path('about/', AboutPageView.as_view(), name='about'),
]
