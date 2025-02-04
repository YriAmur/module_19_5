from django.contrib import admin
from .models import Game, Buyer, News

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size в списке
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение кол-ва записей до 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображение полей name, balance и age в списке
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение кол-ва записей до 30
    readonly_fields = ('balance',)  # Поле balance доступно только для чтения

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Поля, которые будут отображаться в списке
    list_filter = ('date',)  # Фильтры по полю date
    search_fields = ('title', 'content')  # Поиск по полям title и content
    ordering = ('-date',)  # Сортировка по дате (новые сначала)

