from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Daily_Offers(CMSPlugin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="daily_offers")
    description = models.TextField()
    url = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Daily Offer"
        verbose_name_plural = "Daily Offers"


    def __str__(self):
        return "%s"%(self.name)



class Offers(CMSPlugin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="offers")
    price = models.FloatField()
    description = models.TextField()
    url = models.CharField(max_length=200)



    def __str__(self):
        return "%s"%(self.name)