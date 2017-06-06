#coding=utf-8
from django.db import models

# Create your models here.
from django.utils import timezone

from root.models import RoomUseTime


class RoomReserve(models.Model):
    ROOM_TYPE = (
        ('small', '小包'),
        ('middle', '中包'),
        ('large', '大包')
    )
    ROOM_STATUS = (
        (0, '占用'),
        (1, '空闲')
    )
    type = models.CharField(max_length=10, choices=ROOM_TYPE, verbose_name='种类')
    room_number = models.IntegerField(verbose_name=u'房间编号')
    current_use = models.IntegerField(choices=ROOM_STATUS, verbose_name=u'当前空闲')
    name = models.CharField(max_length=255, choices=ROOM_TYPE, verbose_name='名称')

    def __str__(self):
        return self.type + '_' + str(self.id)

    class Meta:
        managed = False
        db_table = 'room_reserve'
        verbose_name = u'房间预订'
        verbose_name_plural = verbose_name


class RoomCall(models.Model):
    room_number = models.IntegerField(verbose_name=u'房间编号')
    call_time = models.DateTimeField(verbose_name=u'呼叫时间')

    class Meta:
        managed = False
        db_table = 'room_call'
        verbose_name = u'呼叫信息'
        verbose_name_plural = verbose_name


class UserRoom(models.Model):
    user_name = models.CharField(max_length=255, verbose_name=u'用户姓名')
    user_phone = models.CharField(max_length=255, verbose_name=u'手机号')
    room_number = models.IntegerField(verbose_name=u'房间号')
    start_time = models.CharField(max_length=255, verbose_name=u'开始时间')
    end_time = models.CharField(max_length=255, verbose_name=u'结束时间')

    class Meta:
        managed = False
        db_table = 'user_room'
        verbose_name = u'用户房间'
        verbose_name_plural = verbose_name