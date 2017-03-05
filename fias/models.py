from django.db import models


class AddrObj(models.Model):
    IFNSFL = models.IntegerField()
    IFNSUL = models.IntegerField()
    OKATO = models.IntegerField()
    OKTMO = models.IntegerField()
    postal_code = models.IntegerField()
    status = models.BooleanField()
    update_date = models.DateField()
    formal_name = models.CharField(max_length=200)
    official_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.official_name
