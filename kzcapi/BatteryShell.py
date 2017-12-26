from django.http import JsonResponse, HttpResponse

from kzcapi.models import BatteryCore, BatteryShell


def batterycore_add(request):
    response_data = {}
    if request.method == 'POST':
        code1 = request.POST.get('code1', '5x13')
        code2 = request.POST.get('code2', None)
        date = request.POST.get('date', None)
        print('batterycore_add method:', request.method)
        print('code1:', code1)
        print('code2:', code2)
        print('date:', date)
        try:
            BatteryCore.objects.create(plastic_carve_code_1=code1,plastic_carve_code_2=code2)
            BatteryShell.objects.create(plastic_carve_code_1=code1,plastic_carve_code_2=code2)
            response_data['result'] = 'true'
            response_data['dec'] = '添加数据成功'
            # response_data['data'] = serializers.serialize('json', data)
            response_data['data'] = ''
        except:
            response_data['result'] = 'false'
            response_data['dec'] = '发生异常，添加数据失败'
            response_data['data'] = ''
    elif request.method == 'GET':
        response_data['result'] = 'false'
        response_data['dec'] = '请求方式错误，需要POST'
        response_data['data'] = ''
    return HttpResponse(JsonResponse(response_data), content_type='application/json;charset=utf-8')
