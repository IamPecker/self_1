"""bashion_ktv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from customer.views import index_customer
from counter.views import index_counter
from website.views import index_website, reserve_website, search_website,selectsong_website, callbar_website
from django.contrib.auth.views import logout
from root.api import room, room_ch
from root.views import *
from django.conf.urls.static import static
import settings
from settings import *
from django import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index_main, name='index'),
    # url(r'^counter/',counter.urls),
    url(r'^root/money/today$', get_today_money, name='today_money'),
    url(r'^root/money/month$', get_current_month_money, name='month_money'),
    url(r'^customer/index/$', index_customer, name='index_customer'),
    url(r'^counter/index/$', index_counter, name='index_counter'),
    url(r'^website/index/$', index_website, name='index_website'),
    url(r'^website/reserve/$', reserve_website, name='reserve_website'),
    url(r'^website/search/$', search_website, name='search_website'),
    url(r'^website/selectsong/$', selectsong_website, name='selectsong_website'),
    url(r'^website/callbar_website/$', callbar_website, name='callbar_website'),
    url(r'^api/room/$', room, name='api_room'),
    url(r'^api/room_ch/(?P<id>\d+)$', room_ch, name='api_room_ch'),
    url(r'^login/$', login_main, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/', logout, {'next_page': '/index'}, name="logout"),
    # url(r'^media/(?P<path>.*)/$', views.static.serve, {"document_root": MEDIA_ROOT}),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url(r'^',index_main),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
