from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'ashu','age':4}
    return render(request,'jinja.html',context=d)