from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView

from apps.forms import RegisterModelForm, LoginModelForm, ReviewModelForm
from apps.models import Book, Review


# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'apps/home.html'


class RegisterFormView(FormView):
    form_class = RegisterModelForm
    template_name = 'apps/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error[0])
        return super().form_invalid(form)


class LoginFormView(FormView):
    form_class = LoginModelForm
    template_name = 'apps/login.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.user
        login(self.request , user)
        return super().form_valid(form)





class HomeListView(ListView):
    queryset = Book.objects.all()
    context_object_name = 'book_list'
    template_name = 'apps/home.html'

class ReviewListView(ListView ):
    queryset = Review.objects.all()
    context_object_name = 'reviews'
    template_name = 'apps/review.html'



class ReviewDetailView(FormView):
    queryset = Review.objects.all()
    form_class = ReviewModelForm
    template_name = 'apps/add-review.html'
    success_url = reverse_lazy('review')







