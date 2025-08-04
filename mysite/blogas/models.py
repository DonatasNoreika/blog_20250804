from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=200)
    body = models.TextField(verbose_name="Turinys")
    created_at = models.DateTimeField(verbose_name="Sukurta", auto_now_add=True)
    published = models.BooleanField(verbose_name="Paskelbta", default=True)

    class Meta:
        verbose_name = "Įrašas"
        verbose_name_plural = "Įrašai"

    def __str__(self):
        return self.title