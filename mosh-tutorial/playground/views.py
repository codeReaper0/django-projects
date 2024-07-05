"""
Returns a simple HttpResponse with the message "Hello world".

Args:
    request: HttpRequest object representing the request made to the server.

Returns:
    HttpResponse: Response object with the message "Hello world".
"""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return render(request, 'hello.html')
