from django.db import models

# Create your models here.




# class Orderitem(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     productname = models.CharField(db_column='productName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     price = models.FloatField(blank=True, null=True)
#     amount = models.BigIntegerField(blank=True, null=True)
#     subtotal = models.FloatField(blank=True, null=True)
#     orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'orderitem'




