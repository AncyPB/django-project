from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index-page"),
    path('index',views.index,name="home-page"),
    path('signup',views.signup,name="signup-page"),
    path('login',views.login,name="login-page"),
    path('home',views.home,name="home-page"),
    path('view',views.view,name="view-page"),
    path('views',views.views,name="view-page"),
    path('owner',views.owner,name="owner-page"),
    path('review',views.review,name="review-page"),
    path('reserve',views.reserve,name='reserve-page'),
    path('viewreview',views.viewreview,name='viewreview'),
    path('hotel',views.hotel,name='hotel'),
]
