from django.contrib import admin

# Register your models here.
from kzcapi.models import CcdCheck, BatchCode, PlasticBox,BatteryCore,BatteryShell


class AdminBatchCode(admin.ModelAdmin):
	list_display = ('id','batch_code','batch_code_date')
	# list_editable = ('batch_code','batch_code_date')
admin.site.register(BatchCode,AdminBatchCode)

# class AdminCcdCheck(admin.ModelAdmin):
# 	list_display = ('id','plastic_carve_code','plastic_battery_check_pic_path','plastic_battery_check_date','plastic_battery_check_status')
# 	# list_editable = ('plastic_carve_code','plastic_battery_check_pic_path','plastic_battery_check_date','plastic_battery_check_status')
# admin.site.register(CcdCheck,AdminCcdCheck)

class AdminPlasticBox(admin.ModelAdmin):
	list_display = ('id','plastic_type','plastic_carve_code', 'plastic_carve_scan_date','plastic_batter_over_date','plastic_battery_check_pic_path','plastic_battery_check_date','plastic_battery_check_status',
					'plastic_battery_check_ng_scan_date',
					'plastic_fixture_scan_date',
					'plastic_battery_soldering_data',
					'plastic_battery_soldering_date',
					'plastic_soldering_a_check_date',
					'plastic_soldering_b_check_date',
					'plastic_soldering_a_check_status',
					'plastic_soldering_b_check_status',
					'plastic_soldering_ng_check_date',
					'plastic_soldering_ab_check_static')
admin.site.register(PlasticBox,AdminPlasticBox)


#BatteryCore电芯测试数据表
class AdminBatteryCore(admin.ModelAdmin):
	list_display = ('id','plastic_carve_code_1','plastic_carve_code_2','heap_battery_core_date','battery_core_scan_date','battery_core_check_status')
admin.site.register(BatteryCore,AdminBatteryCore)

# BatteryShell壳体码数据表
class AdminBatteryShell(admin.ModelAdmin):
	list_display = ('id','plastic_carve_code_1','plastic_carve_code_2','box_shell_code','box_shell_code_date','insulation_check_date','insulation_check_status','module_down_scan_date')
	list_editable = ('box_shell_code',)
admin.site.register(BatteryShell,AdminBatteryShell)


