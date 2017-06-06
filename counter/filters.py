# coding=utf-8
from django.contrib import admin


class RoomStatusFilter(admin.SimpleListFilter):
    title = u'房间状态'
    parameter_name = 'room_status_filter'
    def lookups(self, request, model_admin):
        return ((0, u'空闲'),
                (1, u'使用中'))

    def queryset(self, request, queryset):
        value = self.value()
        return queryset.filter()