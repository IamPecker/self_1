# coding=utf-8
from django import forms
from django.core.exceptions import ValidationError


def word_validator(comment):
    if len(comment) < 4:
        raise ValidationError("not enough words")


def comment_validator(comment):
    keywords = [u"发票", u"钱"]
    for keyword in keywords:
        if keyword in comment:
            raise ValidationError("Your comment contains invalid words,please check it again.")


def length_validator(comment):
    if len(comment) != 11:
        raise ValidationError('手机号不正确。')


def people_num(num):
    if int(num) < 1:
        raise ValidationError('莫非是火星人来过？(没有人啦！)')
    if int(num) > 13:
        raise ValidationError('So Sorry.我们是一家Fashion的歌厅。您的容量有些拥挤喽。(人数多于13人，可电话预定。110-12345678)')


class ReserveForm(forms.Form):
    ROOM_TYPE = (
        ('small', '小包'),
        ('middle', '中包'),
        ('large', '大包')
    )
    name = forms.CharField(max_length=50, label='姓名')
    # phone = forms.CharField(
    #     widget=forms.Textarea(),
    #     error_messages = {
    #         "required": 'wow, such words'
    #         },
    #     validators = [word_validator, comment_validator]
    #     )
    phone = forms.CharField(
        label='手机',
        validators=[length_validator]
    )
    room_type = forms.IntegerField(
        label='房间类型',
        widget=forms.Select(choices=ROOM_TYPE),
    )
