from django.urls import path
from .views import home, create, results,vote


urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('results/<poll_id>', results, name="results"),
    path('vote/<poll_id>', vote, name="vote"),
]



