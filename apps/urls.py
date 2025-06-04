from django.urls import path

from apps.views import HomeListView, RegisterFormView, LoginFormView, ReviewDetailView, ReviewListView

urlpatterns = [

    path('', HomeListView.as_view(), name='home'),
    path('revgister', RegisterFormView.as_view(), name='register'),
    path('login', LoginFormView.as_view(), name='login'),
    path('review', ReviewListView.as_view(), name='review'),
    path('add-r', ReviewDetailView.as_view(), name='add_review'),




]
