from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.title}"



# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey(Category, related_name="category_post_ids", on_delete=models.CASCADE)
    content = models.TextField()


    def __str__(self):
        return f"{self.title}"






