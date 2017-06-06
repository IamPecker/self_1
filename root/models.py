#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
import time
import datetime
from django.utils import timezone
# Create your models here.


class Room(models.Model):
    ROOM_TYPE = (
        ('small', '小包'),
        ('middle', '中包'),
        ('large', '大包')
    )
    type = models.CharField(max_length=10, choices=ROOM_TYPE, verbose_name='种类')
    room_number = models.IntegerField(verbose_name=u'房间编号')
    name = models.CharField(max_length=255, verbose_name=u'房间名称')

    def show_use(self):
        used_times = RoomUseTime.objects.filter(room_number=self.room_number)
        if len(list(used_times))<1:
            return u'空闲'
        # current_time = time.time()
        current_time = timezone.now()
        used_times = [used_time for used_time in used_times]
        for i in range(len(used_times)):
            if current_time>used_times[i].start_time and current_time < used_times[i].end_time:
                return u'已被占用'
        return u'空闲'

    show_use.short_description = u'当前是否在用'

    def __str__(self):
        return self.type + '_' + str(self.id)

    class Meta:
        managed = False
        db_table = 'room'
        verbose_name = u'房间'
        verbose_name_plural = verbose_name


class RoomUseTime(models.Model):
    room_number = models.IntegerField(verbose_name=u'房间编号')
    start_time = models.DateTimeField(verbose_name=u'开始时间')
    end_time = models.DateTimeField(verbose_name=u'结束时间')
    class Meta:
        db_table = 'room_use_time'
        managed = False
        verbose_name = u'房间占用情况'
        verbose_name_plural = verbose_name


class Staff(models.Model):
    GENDER_CHOCIE = (
        (0, '女'),
        (1, '男')
    )
    STATUS_CHOCIE = (
        (0, '在岗'),
        (1, '请假'),
        (2, '缺勤')
    )
    staff_number = models.IntegerField(verbose_name=u'员工编号')
    name = models.CharField(max_length=255, verbose_name=u'姓名')
    gender = models.IntegerField(choices=GENDER_CHOCIE, verbose_name=u'性别')
    age = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOCIE, verbose_name=u'状态')
    join_time = models.DateTimeField(null=True, verbose_name=u"入职时间")

    class Meta:
        managed = False
        db_table = 'staff'
        verbose_name = u'员工'
        verbose_name_plural = verbose_name

class Order(models.Model):
    room_number = models.IntegerField(verbose_name=u'房间编号')
    fee = models.IntegerField(verbose_name=u'收费')
    finish_time = models.DateTimeField(verbose_name=u'交易完成时间')


    class Meta:
        db_table = 'order'
        managed = False
        verbose_name = u'收益情况'
        verbose_name_plural = verbose_name
