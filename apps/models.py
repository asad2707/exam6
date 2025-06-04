from django.db import models
from django.db.models import CharField, DecimalField, DateTimeField, ImageField, Model, ForeignKey, TextField


# Create your models here.



class Book(Model):

    title = CharField(max_length=100)
    author = CharField(max_length=100)
    price = DecimalField(decimal_places=0, max_digits=10)
    image = ImageField(upload_to='images/')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(Model):
    name = CharField(max_length=100)
    book_name = CharField(max_length=100)
    grade = CharField(max_length=100)
    comment = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)




