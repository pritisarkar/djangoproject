from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt
# Create your views here.
@csrf_exempt
def employee(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data['username']
            password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            employee = Employee(username=username, password=hashed_password)
            employee.save()
            return JsonResponse({"msg": "data inserted", "status": "success"})
        else:
            return "hello"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'status': 'error', 'message': str(e)}), 500
    
@csrf_exempt
def fetch_employee(request):
    try:
        if request.method == 'GET':
            employee = Employee.objects.all()
            employee_list = []
            for employee  in employee :
                employee_list.append({'id':employee.id,'username':employee.username})
            return JsonResponse({'msg':"data fetch successfully",'employee':employee_list, 'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Only GET requests are allowed.'}, status=400)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)