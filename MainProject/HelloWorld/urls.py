from django.urls import path
from . import views


urlpatterns = [
    path("", views.Hello , name = 'Hello' ),
    path("<str:name>/", views.HelloName , name = 'HelloName' ),
]
