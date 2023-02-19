from django.urls import path
from .views import SignUpView


urlpatterns = [
    # ex: users/signup
    path('signup/', SignUpView.as_view(), name='signup')
]
