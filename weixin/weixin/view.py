from django.http import HttpResponse
import hashlib

def hello(request):
    return HttpResponse("Hello wordl!")

def AcessConfirm(request):
    if request.method=='GET':
        SignNature = request.GET.get('signature',default='')
        TimeStamp = request.GET.get('timestamp',default='')
        Nonce = request.GET.get('nonce',default = '')
        EchoStr = request.GET.get('echostr',default='')
        if SignNature == '' or TimeStamp == '' or Nonce == '' or EchoStr == '' :
            return HttpResponse('wrong param!')
        Token = ''

        StrList = [Token,TimeStamp,Nonce]
        StrList.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,StrList)
        HashResult = sha1.hexdigest()

        if HashResult == SignNature :
            return HttpResponse(EchoStr)
        


