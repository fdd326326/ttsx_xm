from django.db import models


class CartInfo(models.Model):
    '''购物车'''
    user=models.ForeignKey('tt_user.UserInfo')
    goods=models.ForeignKey('tt_goods.GoodsInfo')
    count=models.IntegerField()

