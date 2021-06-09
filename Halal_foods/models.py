from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Foods(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(models.Model):
    nums = models.IntegerField()
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name