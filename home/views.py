from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    webview='''
    <h2>I am http://3.108.108.136/</h2>
    <h1><a href="http://3.108.108.136/">Refresh</a></h1>
    <p>For more Details <a href="https://www.instagram.com/jade_emperror/">click here</a></p>
        '''
    return HttpResponse(webview)