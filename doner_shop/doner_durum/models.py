from django.db import models
from cms.models.pluginmodel import CMSPlugin


class Daily_Specials(CMSPlugin):
    name= models.CharField(max_length=200)
    image = models.ImageField(upload_to='Daily Specials')
    description = models.TextField()
    url = models.CharField(max_length=200)



    class Meta:
        verbose_name = "Daily Special"
        verbose_name_plural = "Daily Specials"


    def __str__(self):
        return self.name
# Create your models here.
