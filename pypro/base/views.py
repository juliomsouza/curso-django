from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá Django, Julinho aqui..!!!</body></html>', content_type='text/html')
