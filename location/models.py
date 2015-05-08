from django.db import models



class Position(models.Model):

    latitude = models.CharField(blank=False, max_length=500)

    longitude = models.CharField(blank=False, max_length=500)

    phone = models.IntegerField(blank=False)

    count = models.IntegerField(blank=False)

    class Meta:

        verbose_name = 'Position'

        verbose_name_plural = 'Positions'

    def __unicode__(self):

        return "%s , %s" %(self.latitude, self.longitude)
