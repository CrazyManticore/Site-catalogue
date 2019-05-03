from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название альбома')
    description = models.TextField(verbose_name='Описание альбома')
    image = models.URLField(max_length=300,verbose_name='Ссылка на Обложку альбома', default='')

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40, verbose_name='Название песни')
    video_url = models.URLField(max_length=200, verbose_name='Ссылка на видео', default='')
    text = models.TextField(verbose_name='Текст песни', default='')
    translate = models.TextField(verbose_name='Перевод песни', default='')

    def __str__(self):
        return self.name