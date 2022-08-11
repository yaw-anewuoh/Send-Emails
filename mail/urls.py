from django.urls import path
from .views import ContactView,ContactSuccessView

urlpatterns=[
    path('',ContactView.as_view(),name='home'),
    path('success/',ContactSuccessView.as_view(),name='success')
]