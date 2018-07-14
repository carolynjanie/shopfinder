from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
# from django.contrib.gis.db.models.manager import GeoManager
# from django.db.models import Manager as GeoManager

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)

    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.name
