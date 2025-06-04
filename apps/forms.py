from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.models import Review


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = 'username', 'email' , 'password' ,'first_name'

    def clean_password(self):
        return make_password(self.cleaned_data.get("password"))

    def save(self, commit = False):
        data = self.cleaned_data
        return User.objects.create(**data)


class LoginModelForm(ModelForm):
    class Meta:
        model = User
        fields = 'username', 'password'

    def __init__(self, *args, **kwargs):


        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)


    # class Meta:
    #     model = User
    #     fields = "email", "password"


    def clean(self):
        data = self.cleaned_data
        username = data.get("username")
        password = data.get("password")
        query = User.objects.filter(username=username)
        if query.exists():
            user = query.first()
            if not check_password(password, user.password):
                raise ValidationError("password xato")
            self.user = user
        else:
            raise ValidationError("Topilmadi ")
        return data


class ReviewModelForm(ModelForm):
    class Meta:
        model = Review
        fields = 'book_name' , 'grade' , 'name' , 'comment'

    def save(self, commit = False):
        data = self.cleaned_data
        return Review.objects.create(**data)