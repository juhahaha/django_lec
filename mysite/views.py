# from django.http import HttpResponse
from django.shortcuts import  get_object_or_404, render
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request, content_id): # 매개변수 content_id 추가 url의 2 의미
     content_list =  get_object_or_404(MainContent, pk=content_id)
     context = { 'content_list': content_list}
     return render(request, 'mysite/content_detail.html', context)
