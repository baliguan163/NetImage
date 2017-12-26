from django.conf.urls import url

from kzcapi import BatchCode, PlasticBox, BatteryShell
from . import views

urlpatterns = [
    # url(r'^ccddata/$', views.ccddata, name='ccddata'),
    #
    # url(r'^datasave/$', views.datasave, name='datasave'),

    #--------------------------------------------------------------
    url(r'^batchcode/list/$', BatchCode.batchcode_list, name='batchcode_list'),
    url(r'^batchcode/detail/$', BatchCode.batchcode_detail, name='batchcode_detail'),
    url(r'^batchcode/delete/$', BatchCode.batchcode_delete, name='batchcode_delete'),
    url(r'batchcode/add$', BatchCode.batchcode_add, name='batchcode_add'),
    url(r'^batchcode/update$', BatchCode.batchcode_update, name='batchcode_update'),


    #-------------------------------------------------------------------------
    url(r'^plasticbox/add$', PlasticBox.plasticbox_add, name='plasticbox_add'),

    # -------------------------------------------------------------------------
    url(r'^batterycore/add$', BatteryShell.batterycore_add, name='batterycore_add'),



    # url(r'^batchcode_delete/([0-9]+)$', views.batchcode_delete, name='batchcode_delete'),
    # url(r'^batchcode_update/([0-9]+)$', views.batchcode_update, name='batchcode_update'),
    # url(r'batchcode_add/$', views.batchcode_add, name='batchcode_add'),

    # url(r'list/$', views.get_xx_tabs, ),
    # url(r'detail/([0-9]+)$', views.get_xx_tab),
    #
    # url(r'delete/([0-9]+)$', views.delete_xx_tab),
    #
    # url(r'update/([0-9]+)$', views.update_xx_tab),
    #
    # url(r'add/$', views.add_xx_tab),

]
