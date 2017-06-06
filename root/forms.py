#coding=utf-8
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField

from counter.models import RoomReserve
from models import Room

# def word_validator(comment):
#     if len(comment) < 4:
#         raise ValidationError("not enough words")
#
# def comment_validator(comment):
#     keywords = [u"发票", u"钱"]
#     for keyword in keywords:
#         if keyword in comment:
#             raise ValidationError("Your comment contains invalid words,please check it again.")
#
# class CommentForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     comment = forms.CharField(
#         widget=forms.Textarea(),
#         error_messages = {
#             "required": 'wow, such words'
#             },
#         validators = [word_validator, comment_validator]
#         )
from root.models import Staff


class RoomModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomModelForm, self).__init__(*args, **kwargs)

    def clean_room_number(self):
        room_number = self.cleaned_data['room_number']
        rooms = Room.objects.filter(room_number=room_number)
        room_count = len(list(rooms))
        if room_count > 0:
            if not self.instance.id:
                raise ValidationError(u'该房间编号已经存在，请重新设置房间编号')
            else:
                rooms = [room for room in rooms]
                for i in range(room_count):
                    if rooms[i].id != self.instance.id:
                        raise ValidationError(u'该房间编号已经存在，请重新设置房间编号')
        return room_number

    def save(self, commit=True):
        return super(RoomModelForm, self).save(commit)


    class Meta:
        model = Room
        exclude = ('id',)


class StaffModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StaffModelForm, self).__init__(*args, **kwargs)

    def clean_staff_number(self):
        staff_number = self.cleaned_data['staff_number']
        staffs = Staff.objects.filter(staff_number=staff_number)
        staff_count = len(list(staffs))
        if staff_count > 0:
            if not self.instance.id:
                raise ValidationError(u'该员工编号已经存在，请重新设置')
            else:
                staffs = [staff for staff in staffs]
                for i in range(staff_count):
                    if staffs[i].id != self.instance.id:
                        raise ValidationError(u'该员工编号已经存在，请重新设置')
        return staff_number

    class Meta:
        model = Staff
        exclude = ('id',)


class RoomReserveModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomReserveModelForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        return super(RoomReserveModelForm, self).save(commit)

    class Meta:
        model = RoomReserve
        exclude = ('id', )

