from time import ctime, timezone, time

import simplejson as simplejson
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from kzcapi.models import CcdCheck, BatchCode

#
# def index(request):
#     return render(request,'index.html')
#
# def upload(request):
#
#
# http://127.0.0.1:8000/jsondemo/getpdata
from django.shortcuts import get_object_or_404, render



# 如果是GET，需要处理request .query_params；如果是post需要处理request .data
# if request.method == 'GET':
#     for k in request .query_params:  
#     dict[k] = request .query_params[k]
#     return dictel
#
# if request.method == 'POST':
#     for k in request.data
#         dict[k] = request .data [k]
#         return dict

# return render(request, 'polls/detail.html', {'question': question})

# http://127.0.0.1:8000/kzcapi/batchcode/detail/?pk_id=1
def batchcode_list(request):
    response_data = {}
    #print('data:', request.method)
    if request.method == 'GET':
        data = BatchCode.objects.order_by('pk')
        try:
            if(data):
                response_data['result'] = 'true'
                response_data['dec'] = '获取成功'
                response_data['data'] = serializers.serialize('json', data)
            else:
                response_data['result'] = 'false'
                response_data['dec'] = '获取失败，数据不存在'
                response_data['data'] = serializers.serialize('json', data)
        except:
            response_data['result'] = 'false'
            response_data['dec'] = '发生异常'
            response_data['data'] = ''
    elif request.method == 'POST':
        response_data['result'] = 'false'
        response_data['dec'] = '请求方式错误，需要GET'
        response_data['data'] = ''
    return HttpResponse(JsonResponse(response_data), content_type='application/json;charset=utf-8')


# http://127.0.0.1:8000/kzcapi/batchcode/detail/?detail=1
def batchcode_detail(request):
    response_data = {}
    print('data:', request.method)
    if request.method == 'GET':
        pk_id = request.GET.get("id", None)
        print('id:', pk_id)
        data = BatchCode.objects.filter(pk=pk_id)
        try:
            if(data):
                response_data['result'] = 'true'
                response_data['dec'] = '获取成功'
                response_data['data'] = serializers.serialize('json', data)
            else:
                response_data['result'] = 'false'
                response_data['dec'] = '获取失败，数据不存在'
                response_data['data'] = serializers.serialize('json', data)
        except:
            response_data['result'] = 'false'
            response_data['dec'] = '发生异常'
            response_data['data'] = ''
    elif request.method == 'POST':
        response_data['result'] = 'false'
        response_data['dec'] = '请求方式错误，需要GET'
        response_data['data'] = ''
    return HttpResponse(JsonResponse(response_data), content_type='application/json;charset=utf-8')

def batchcode_delete(request):
    response_data = {}
    print('batchcode_delete method:', request.method)
    if request.method == 'GET':
        id = request.GET.get("id", None)
        print('id:', id)
        data = BatchCode.objects.filter(pk=id)
        try:
            if (data):
                delete_count = data.delete();
                print('delete_count:', delete_count)
                response_data['result'] = 'true'
                response_data['dec'] = '数据删除成功'
                response_data['data'] = serializers.serialize('json', data)

            else:
                response_data['result'] = 'false'
                response_data['dec'] = '数据不存在，数据删除失败'
                response_data['data'] = serializers.serialize('json', data)
        except:
                response_data['result'] = 'false'
                response_data['dec'] = '发生异常，数据删除失败'
                response_data['data'] = ''
    elif request.method == 'POST':
        response_data['result'] = 'false'
        response_data['dec'] = '请求方式GET错误，数据删除失败'
        response_data['data'] = ''
    return HttpResponse(JsonResponse(response_data), content_type='application/json;charset=utf-8')


def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def batchcode_add(request):
    response_data = {}
    if request.method == 'POST':
        code = request.POST.get('code', None)
        date = request.POST.get('date', None)
        print('batchcode_add method:', request.method)
        print('code:', code)
        print('date:', date)
        try:
            # systime = GetNowTime()
            # print('timezone.now:',time.time())
            BatchCode.objects.create(batch_code=code)
            data = BatchCode.objects.filter(batch_code=code)
            response_data['result'] = 'true'
            response_data['dec'] = '添加数据成功'
            response_data['data'] = serializers.serialize('json', data)
        except:
            response_data['result'] = 'false'
            response_data['dec'] = '发生异常，添加数据失败'
            response_data['data'] = ''
    elif request.method == 'GET':
        response_data['result'] = 'false'
        response_data['dec'] = '请求方式错误，需要POST'
        response_data['data'] = ''
    return HttpResponse(JsonResponse(response_data), content_type='application/json;charset=utf-8')

def batchcode_update(request):
    response_data = {}
    if request.method == 'POST':
        id = request.POST.get('id', None)
        code = request.POST.get('code', None)
        print('id:', id)
        print('code:', code)
        try:
            if (id):
                update_count = BatchCode.objects.filter(pk=id).update(batch_code=code)
                print('update_count:', update_count)
                data = BatchCode.objects.filter(pk=id)
                # batchcode_data = BatchCode.objects.create(batch_code=code,batch_code_date=date)
                # BatchCode.add(batchcode_data)
                response_data['result'] = 'true'
                response_data['dec'] = '更新数据成功'
                response_data['data'] = serializers.serialize('json', data)
            else:
                response_data['result'] = 'false'
                response_data['dec'] = '参数为空，更新数据失败'
                response_data['data'] = ''
        except:
                response_data['result'] = 'false'
                response_data['dec'] = '发生异常，更新数据失败'
                response_data['data'] = ''
    elif request.method == 'GET':
        response_data['result'] = 'false'
        response_data['dec'] = '请求方式GET错误，更新数据失败'
        response_data['data'] = ''
    return HttpResponse(JsonResponse(response_data), content_type='application/json;charset=utf-8')

    #
    # if request.method == 'GET':
    #     pk_id = request.GET.get("pk_id", None)
    #     print('pk_id:', pk_id)
    #     # data =   get_object_or_404(BatchCode, pk=pk_id)
    #     data = BatchCode.objects.filter(pk=pk_id)
    #     try:
    #         if (data):
    #             response_data['result'] = 'true'
    #             response_data['dec'] = '数据删除成功'
    #             response_data['data'] = serializers.serialize('json', data)
    #             data.delete();
    #         else:
    #             response_data['result'] = 'false'
    #             response_data['dec'] = '数据不存在，无法删除'
    #             response_data['data'] = serializers.serialize('json', data)
    #     except:
    #             response_data['result'] = 'false'
    #             response_data['dec'] = '发生异常，删除失败'
    #             response_data['data'] = ''
    # elif request.method == 'POST':
    #     response_data['result'] = 'false'
    #     response_data['dec'] = '请求方式错误，需要GET，删除失败'
    #     response_data['data'] = ''
    # return HttpResponse(JsonResponse(response_data), content_type='application/json')
    #





    # if request.method == 'GET':
    #
    #
    #
    #     for k in request.query_params:
    #         dict[k] = request.query_params[k]
    #     return dict
    # elif request.method == 'POST':
    #     for k in request.data:
    #         dict[k] = request.data[k]
    #     return dict
    # print('pk_id:', pk_id)
    # if request.method == 'GET':
    #
    #     # GETid = request.GET.get('pk_id')
    #     # timestamp = request.GET.get('timestamp')
    #     # for k in request.query_params:
    #     #     dict[k] = request.query_params[k]
    #     # print('data:', request)
    #     # # data = BatchCode.objects(pk=question_id)
    #     # data = get_object_or_404(BatchCode, pk=id)
    #     # try:
    #     #     if(data):
    #     #         response_data['result'] = '1'
    #     #         response_data['dec'] = 'success'
    #     #         response_data['data'] = serializers.serialize('json', data)
    #     #     else:
    #     #         response_data['result'] = '0'
    #     #         response_data['dec'] = 'fail'
    #     #         response_data['data'] = serializers.serialize('json', data)
    #     # except:
    #     #     response_data['result'] = '0'
    #     #     response_data['dec'] = 'exception'
    #     #     response_data['data'] = ''
    # if request.method == 'POST':
    #     for k in request.body:
    #         print('request data:', request.body[k])
    #     # response_data['result'] = '0'
    #     # response_data['dec'] = 'must post'
    #     # response_data['data'] = ''
    # return HttpResponse(JsonResponse(response_data), content_type='application/json')


# http://127.0.0.1:8000/kzcapi/ccddata
# http://192.168.0.125:8000/kzcapi/ccddata
# def ccddata(request):
#     print('data:', request.method)
#     data = BatchCode.objects.order_by('id')
#     print('data:',data)
#     response_data = {}
#     try:
#         if (data):
#             response_data['result'] = '1'
#             response_data['dec'] = '获取成功'
#             response_data['data'] = serializers.serialize('json', data)
#         else:
#             response_data['result'] = '0'
#             response_data['dec'] = '获取失败'
#             response_data['data'] = serializers.serialize('json', data)
#     except:
#         response_data['result'] = '0'
#         response_data['dec'] = 'exception'
#         response_data['data'] = ''
#     return HttpResponse(JsonResponse(response_data), content_type='application/json')
#
#
# def addccd(request):
#     print('data:', request.method)
#     print('body:', request.body)
#     if request.method=='POST':
#         # req=json.loads(request.body)
#         req = simplejson.loads(request.raw_post_data)
#         ccd_data=list()
#         for value in req.items():
#             ccd_data.append({
#                     'plastic_carve_code':value.get('code'),
#                     'plastic_battery_check_pic_path':value.get('path'),
#                     'plastic_battery_check_date':value.get('date'),
#                     'plastic_battery_check_status':value.get('status')})
#         CcdCheck.objects.bulk_create(ccd_data)
#         response_data = {}
#         response_data['result'] = '1'
#         response_data['dec'] = '添加成功'
#         return HttpResponse(JsonResponse(response_data), content_type='application/json')
#
#
# # equest.raw_post_data表示的是从客户端发送过来的原始数据,为了纯字符串, 通过simplejson的loads方法将其转换为字典数据类型req.
# # 上面的代码也演示了如何以JSON格式作为响应值, 而非HTML, 即通过simplejson的dumps方法, 将字典数据dict序列化为字符串形式,将通过HttpResponse返回.
# def batchcode_detail(request):
#     if 'id' in request.GET:
#         fid=request.GET['id']
#         userCollectList=serializers.serialize("json",BatchCode.objects.filter(pk = fid))
#         return HttpResponse(userCollectList, content_type='application/json; charset=utf-8')
#     #



# def batchcode_detail(request):
#     dict = {}
#     info = 'data success'
#     try:
#         if request.method == 'POST':
#             req = simplejson.loads(request.raw_post_data)
#             print('req:',req)
#             plastic_carve_code = req['code']
#             plastic_battery_check_pic_path = req['path']
#             plastic_battery_check_date    = req['date']
#             plastic_battery_check_status = req['status']
#             print('plastic_carve_code:',plastic_carve_code)
#     except:
#         import sys
#         info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
#     dict['result'] = '1'
#     dict['dec'] = info
#     dict['date'] = str(ctime())
#     # dict['date'] = str(ctime())
#     ctimejson = simplejson.dumps(dict)
#     print("json:",ctimejson)
#     return HttpResponse(ctimejson)


# def datasave(request):
#     dict = {}
#     info = 'Data log save success'
#     try:
#         if request.method == 'POST':
#             req = simplejson.loads(request.raw_post_data)
#             print('req:',req)
#             plastic_carve_code = req['code']
#             plastic_battery_check_pic_path = req['path']
#             plastic_battery_check_date    = req['date']
#             plastic_battery_check_status = req['status']
#             print('plastic_carve_code:',plastic_carve_code)
#     except:
#         import sys
#         info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
#     dict['result'] = '1'
#     dict['dec'] = info
#     dict['date'] = str(ctime())
#     # dict['date'] = str(ctime())
#     ctimejson = simplejson.dumps(dict)
#     print("json:",ctimejson)
#     return HttpResponse(ctimejson)
