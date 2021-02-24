from django.shortcuts import render
from django.http import JsonResponse
from .models import SignupModel
# Create your views here.
def validate_details(request):
    print("\n request.POST",request.POST)
    name = request.POST.get('name')
    print("\n name:",name)
    data = {
        'is_taken': SignupModel.objects.filter(name__iexact=name).exists()
    }
    print("\n data:",data)
    return JsonResponse(data)


def signup_view(reqeust):
    temp = 'signup.html'
    if reqeust.method == 'POST':
        name = reqeust.POST.get('name')
        email = reqeust.POST.get('email')
        passwd = reqeust.POST.get('password')
        conf_passwd = reqeust.POST.get('confirm_password')
        sign_obj = SignupModel(name=name,email=email,password=passwd,confirm_password=conf_passwd)
        sign_obj.save()


    return render(reqeust,temp)

