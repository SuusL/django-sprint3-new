from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedModel, CreatedModel


User = get_user_model()

TITLE_MAX_LENGTH = NAME_MAX_LENGTH = 256
CATEGORY_STR_MAX_LENGTH = 30


class Post(PublishedModel, CreatedModel):
    """Модель Публикация."""

    title = models.CharField('Заголовок', max_length=TITLE_MAX_LENGTH)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации',
                                    help_text='Если установить дату и время в '
                                    'будущем — можно делать отложенные '
                                    'публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts',
    )

    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
        related_name='posts',
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Category(PublishedModel, CreatedModel):
    """Модель Категория."""

    title = models.CharField('Заголовок', max_length=TITLE_MAX_LENGTH)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор',
                            help_text='Идентификатор страницы для URL; '
                            'разрешены символы латиницы, цифры, дефис и '
                            'подчёркивание.',
                            unique=True)

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:CATEGORY_STR_MAX_LENGTH]


class Location(PublishedModel, CreatedModel):
    """Модель Местоположение."""

    name = models.CharField('Название места', max_length=NAME_MAX_LENGTH)

    class Meta():
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
