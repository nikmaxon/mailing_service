from django.db import models
from django.utils.timezone import now

NULLABLE = {
    'blank': True,
    'null': True
}


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    img = models.ImageField(verbose_name='изображение', **NULLABLE)
    count_views = models.IntegerField(default=0, verbose_name='количество просмотров', **NULLABLE)
    date_published = models.DateTimeField(default=now, verbose_name='дата публикации', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано', **NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
