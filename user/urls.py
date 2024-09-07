from django.urls import path,include


from .views import Login, Join

urlpatterns = [

    path('join', Join.as_view(), name='join'),
    path('login', Login.as_view(), name='login'),
]