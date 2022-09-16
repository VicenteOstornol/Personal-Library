from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="title")
    image = models.ImageField(upload_to='images/', verbose_name="image", null=True)
    description = models.TextField(verbose_name="description", null=True)

    def __str__(self):
        return f"ID: {self.id} - Title: {self.title} - Description: {self.description}"


    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()