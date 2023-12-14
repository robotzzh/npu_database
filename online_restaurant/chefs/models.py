from django.db import models

# Create your models here.


class dish(models.Model):
    dno = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"this dish is no{self.dno} dish"



class chef(models.Model):
    cno = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"this is no{self.cno}chef"

class dish_chef(models.Model):
    df_no = models.IntegerField(primary_key=True)
    dno = models.IntegerField()
    cno = models.IntegerField()
    Datetime = models.DateField(auto_now=True)
    finished = models.BooleanField(default=False)
    # 创建一个事件
    # event_date='2023-12-01'这样插入

    def __str__(self):
        return f"this Transaction is on {self.Datetime} , its condition is{self.finished}"
