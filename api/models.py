# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TBudgets(models.Model):
    a_shop_id = models.IntegerField(primary_key=True)
    a_month = models.DateField()
    a_budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    a_amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    a_notification = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_budgets'
        unique_together = (('a_shop_id', 'a_month'),)


class TShops(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=255)
    a_online = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_shops'
