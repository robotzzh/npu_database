from django.db import models

# Create your models here.


class eat_in(models.Model):
    Datetime = models.DateField()
    eat_in_no = models.IntegerField(primary_key=True)
    tno = models.IntegerField()# 桌子号
    dno = models.IntegerField()
    comments = models.CharField(max_length=128)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"this transaction is eat_in its condition is{self.finished}"


class take_away(models.Model):
    Datetime = models.DateField()
    take_away_no = models.IntegerField(primary_key=True)
    dno = models.IntegerField()
    comments = models.CharField(max_length=128)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"this transaction is take_away its condition is{self.finished}"