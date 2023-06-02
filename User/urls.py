from django.urls import path
# from User import views


# urlpatterns = [
#     path('/api/user',views.TEST_VIEW)
# ]

from .views import UserView

urlpatterns = [
    path('',UserView.as_view(),name='User'),
]