import json
import uuid

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from .models import Account, Client, Worker

from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET"])
def accs(request):
    return JsonResponse(list(Account.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def acc(request, acc_id):
    acc_item = Account.objects.get(uid=acc_id)
    response_data = {
        'uid': acc_item.uid,
        'name': acc_item.name,
        'description': acc_item.description,
        'client': acc_item.client.uid,
        'worker': acc_item.worker.uid
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def search_acc(request):
    query = request.GET.get('q', '')
    accs = Account.objects.filter(name__icontains=query) | Account.objects.filter(description__icontains=query)
    response_data = {
        'accs': list(accs.values())
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_acc(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        acc_item = Account.objects.create(uid=uid, acc_name=data['name'], acc_discr=data['description'],
                                            client=Client.objects.get(uid=data['client']), worker=Worker.objects.get(uid=data['worker']), acc_money=data['money'])

        response_data = {
            'uid': acc_item.uid,
            'name': acc_item.acc_name,
            'description': acc_item.acc_discr,
            'client': acc_item.client.uid,
            'worker': acc_item.worker.uid,
            'money': acc_item.acc_money
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        print(error)
        return JsonResponse({'error': str(error)}, status=400)


@require_http_methods(["GET"])
def clients(request):
    return JsonResponse(list(Client.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def client(request, client_id):
    client_item = Client.objects.get(uid=client_id)
    response_data = {
        'uid': client_item.uid,
        'first_name': client_item.cl_first_name,
        'last_name': client_item.cl_last_name,
        'number': client_item.cl_number,
        'passport': client_item.cl_passport
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_client(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        client_item = Client.objects.create(uid=uid, cl_first_name=data['first_name'], cl_last_name=data['last_name'],
                                             cl_number=data['number'], cl_passport=data['passport'])

        response_data = {
            'uid': client_item.uid,
            'first_name': client_item.cl_first_name,
            'last_name': client_item.cl_last_name,
            'number': client_item.cl_number,
            'passport': client_item.cl_passport
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=400)


@require_http_methods(["GET"])
def workers(request):
    return JsonResponse(list(Worker.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def worker(request, worker_id):
    worker_item = Worker.objects.get(uid=worker_id)
    response_data = {
        'uid': worker_item.uid,
        'first_name': worker_item.wk_first_name,
        'last_name': worker_item.wk_last_name,
        'position': worker_item.wk_position
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_worker(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        worker_item = Worker.objects.create(uid=uid, wk_first_name=data['first_name'], wk_last_name=data['last_name'],
                                             wk_position=data['position'])

        response_data = {
            'uid': worker_item.uid,
            'first_name': worker_item.wk_first_name,
            'last_name': worker_item.wk_last_name,
            'position': worker_item.wk_position
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=400)
















