from django.db import models
from django.utils import timezone

# Create your models here.


class Buyer(models.Model):
    objects = models
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Баланс
    age = models.IntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    objects = models
    title = models.CharField(max_length=100)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание игры
    age_limited = models.BooleanField(default=False)  # Ограничение по возрасту
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели

    def __str__(self):
        return self.title


from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

