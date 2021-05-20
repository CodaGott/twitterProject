from django.urls import path
from twitterapp import views

urlpatterns = [
    path('', views.home_view, name='post_index'),
    # path('<int:pk>', views.single_post, name='single_post')
]
