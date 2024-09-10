from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50,verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    email = models.EmailField(verbose_name="Почта")
    photo = models.ImageField(upload_to='photo')
    create_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} создал задачу в {self.create_add}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

