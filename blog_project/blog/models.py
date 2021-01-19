from django.db import models
from django.utils import timezone

from django.apps import AppConfig
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20, db_column='GUID')
    name = models.CharField(max_length=30, db_column='NAME', null=False)
    surname = models.CharField(max_length=30, null=False)
    mail = models.EmailField(db_column='MAIL', null=False)
    score = models.FloatField(db_column='USER_SCORE')

    class Meta:
        db_table = "USER"


class Message(models.Model):
    message_id = models.CharField(primary_key=True,
                                  max_length=20,
                                  db_column='MESID')
    context = models.CharField(max_length=1000,
                               db_column='CONTEXT',
                               null=False)
    sendtime = models.DateTimeField(db_column='SENDTIME', default=timezone.now)
    sender = models.ForeignKey(User,
                               db_column='SENDERID',
                               null=False,
                               on_delete=models.CASCADE)

    class Meta:
        db_table = "MESSAGE"


class Price(models.Model):
    price = models.IntegerField(db_column='PRICE')

    class Meta:
        db_table = "SALARY"