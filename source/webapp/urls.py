from django.urls import path

from webapp.views import home_view

urlpatterns = [
    path('', home_view),

]
