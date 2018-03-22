from django.db import models
from .models_gen import *


class CustomBaseModel(models.Model):
    """docstring for CustomBaseModel"""
    class Meta:
        abstract = True


class QuestRewardDataCustom(CustomBaseModel):
    """docstring for QuestRewardData"""
    # maybe we need to use a wide table
    quest = models.ForeignKey(QuestData , default=None , null=True, on_delete=models.CASCADE)
    equipment = models.ForeignKey(EquipmentData, default=None , null=True , on_delete=models.CASCADE)
    item = models.ForeignKey(ItemData, default=None , null=True, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)


# class QuestRewardDataWide(CustomBaseModel):
#     """docstring for QuestRewardData"""
#     # an dirty table for query
#     quest = models.ForeignKey(QuestData , default=None , null=True, on_delete=models.CASCADE)
#     equipment = models.ForeignKey(EquipmentData, default=None , null=True , on_delete=models.CASCADE)
#     item = models.ForeignKey(ItemData, default=None , null=True, on_delete=models.CASCADE)
#     rate = models.FloatField(default=0)