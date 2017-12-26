import django.utils.timezone as timezone

from django.db import models


#BatchCode批次码信息表
class BatchCode(models.Model):
    batch_code=models.CharField('批次信息',max_length=64)
    batch_code_date=models.DateTimeField('生成日期',default=timezone.now)

#CcdCheck相机检测数据表
class CcdCheck(models.Model):
    battery_check_status = (
        ('0', '默认电池正反未检查'),
        ('1', 'CCD检测电池正反OK'),
        ('2', 'CCD检测电池正反NG'),
        ('3', '人工检测电池正反OK'),
    )
    plastic_carve_code=models.CharField('胶框刻码',max_length=64)
    plastic_battery_check_pic_path=models.FileField('图像路径',max_length=128,default='null')
    plastic_battery_check_date=models.DateTimeField('生成日期',default=timezone.now)
    plastic_battery_check_status=models.CharField('检查状态',max_length=1, choices=battery_check_status, default='0')


# PlasticBox胶框信息表
class PlasticBox(models.Model):
    soldering_type = (
        ('5x13', '5x13'),
        ('10x13', '10x13'),
    )

    battery_check_status = (
        ('0', '未检查'),
        ('1', '检测OK'),
        ('2', '检测NG'),
        ('3', '人工检测OK'),
    )
    soldering_check_status = (
        ('0', '未检查'),
        ('1', '检查OK'),
        ('2', '检查NG'),
        ('3', '焊接检查OK'),
    )
    #胶框类型
    plastic_type = models.CharField('类型', max_length=5, choices=soldering_type, default='5x13')
    # 胶框刻码
    plastic_carve_code=models.CharField('胶框刻码',max_length=64,null=True)
    #胶框扫码时间
    plastic_carve_scan_date=models.DateTimeField('扫码胶框时间',default=timezone.now)
    # 胶框装完电池时间
    plastic_batter_over_date=models.DateTimeField('装电池时间',default=timezone.now)
    # 图像路径
    # plastic_battery_check_pic_path = models.FileField('图像路径', max_length=128, default='null')
    plastic_battery_check_pic_path = models.ImageField(upload_to='ccd_image')

    # 生成日期
    plastic_battery_check_date = models.DateTimeField('图像日期',default=timezone.now)
    # CCD检查状态
    plastic_battery_check_status = models.CharField('CCD状态', max_length=1, choices=battery_check_status, default='0')
    #人工电池正反处理时间
    plastic_battery_check_ng_scan_date=models.DateTimeField('电池回流时间',default=timezone.now)
    # 人工扫码放夹具时间
    plastic_fixture_scan_date=models.DateTimeField('人工扫码放夹具时间',default=timezone.now)

    #模组焊接点数据（自定义字符串）
    plastic_battery_soldering_data = models.CharField('模组焊接点数据', max_length=128, default='null')
    plastic_battery_soldering_date = models.DateTimeField('模组焊接时间', default=timezone.now)

    #模组A面焊接检查时间
    plastic_soldering_a_check_date=models.DateTimeField('A焊接面检查时间',default=timezone.now)
    # 模组B面焊接检查时间
    plastic_soldering_b_check_date=models.DateTimeField('B焊接面检查时间',default=timezone.now)

    #模组A面焊接状态
    plastic_soldering_a_check_status=models.CharField('A焊接面状态',max_length=1, choices=soldering_check_status, default='0')
    # 模组B面焊接状态
    plastic_soldering_b_check_status=models.CharField('B焊接面状态',max_length=1, choices=soldering_check_status, default='0')

    #模组AB焊接面NG回流
    plastic_soldering_ng_check_date=models.DateTimeField('焊接面回流时间',default=timezone.now)
    #模组AB面焊接检查状态
    plastic_soldering_ab_check_static=models.CharField('焊接面回流检查状态',max_length=1, choices=soldering_check_status, default='0')

# BatteryCore电芯测试数据表
class BatteryCore(models.Model):
    battery_core_check_status = (
        ('0', '电芯未测试'),
        ('1', '电芯测试OK'),
        ('2', '电芯测试NG'),
    )
    # 胶框刻码1
    plastic_carve_code_1=models.CharField('胶框刻码1',max_length=64,null=True)
    # 胶框刻码2
    plastic_carve_code_2=models.CharField('胶框刻码2',max_length=64,null=True)
    # 堆叠电芯时间
    heap_battery_core_date= models.DateTimeField('电芯堆叠绑定时间', default=timezone.now)
    # 电芯测试扫码时间
    battery_core_scan_date= models.DateTimeField('电芯测试时间', default=timezone.now)
    # 电芯胶框刻码1扫码状态
    battery_core_check_status=models.CharField('电芯测试状态',max_length=1, choices=battery_core_check_status, default='0')

# BatteryShell壳体码数据表
class BatteryShell(models.Model):
    insulation_check_status = (
        ('0', '绝缘未测试'),
        ('1', '绝缘测试OK'),
        ('2', '绝缘测试NG'),
    )
    # 胶框刻码1
    plastic_carve_code_1=models.CharField('胶框刻码1',max_length=64,null=True)
    # 胶框刻码2
    plastic_carve_code_2=models.CharField('胶框刻码2',max_length=64,null=True)
    #壳体码
    box_shell_code=models.CharField('壳体码',max_length=64)
    # 壳体码扫码时间
    box_shell_code_date=models.DateTimeField('壳体码扫码时间', default=timezone.now)
    # 绝缘测试时间
    insulation_check_date=models.DateTimeField('绝缘测试时间', default=timezone.now)
    # 绝缘测试状态
    insulation_check_status=models.CharField('电芯测试状态',max_length=1, choices=insulation_check_status, default='0')
    # 模组下线扫码时间
    module_down_scan_date=models.DateTimeField('壳体码扫码时间', default=timezone.now)


