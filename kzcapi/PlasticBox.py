# 胶框类型
from django.contrib.sessions import serializers
from django.http import JsonResponse, HttpResponse

from kzcapi.models import PlasticBox

def plasticbox_add(request):
    response_data = {}
    if request.method == 'POST':
        type = request.POST.get('type', '5x13')
        code = request.POST.get('code', None)
        date = request.POST.get('date', None)
        print('plasticbox_add method:', request.method)
        print('type:', type)
        print('code:', code)
        print('date:', date)
        try:
            PlasticBox.objects.create(plastic_type=type,plastic_carve_code=code)
            # data = PlasticBox.objects.filter(plastic_carve_code=code)
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

