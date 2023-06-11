from django.db import models

# Create your models here.
"""
MODELs === TABLES
so we created a table called Url
it has the columns, link and uuid
"""

class Url(models.Model):
    link = models.CharField(max_length=10000) # the url to shorten
    uuid = models.CharField(max_length=10) # the uid to shorten it to (appended to the end)