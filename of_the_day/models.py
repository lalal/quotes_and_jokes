from django.db import models

class Otd(models.Model):
    otd_type = models.TextField(verbose_name = "OfTheDay_Type", null=False)
    sub_type = models.TextField(verbose_name = "Sub_Type", null=False)
    api_source = models.TextField(verbose_name = "Api_Source", null=False)
    data = models.TextField(verbose_name = "Data", null=False)
    otd_date = models.TextField(verbose_name = "OfTheDay_Date", null=False)


