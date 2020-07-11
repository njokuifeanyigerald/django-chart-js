from django.urls import path
from .views import Home,LineChart


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('line/', LineChart.as_view(), name="LineChart"),
]



