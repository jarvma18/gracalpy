'''Polls views'''
from django.http import HttpResponse

def index(request):
    '''Index of views'''
    print(request)
    return HttpResponse('Hello, world. You are at the polls index.')
