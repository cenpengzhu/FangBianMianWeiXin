from django.http import HttpResponse
import hashlib
import logging

logger = logging.getLogger('httplogger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('djangoviews.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def hello(request):
    logger.info('Hello wordl!')
    return HttpResponse("Hello wordl!")

def AcessConfirm(request):
    logger.info('AcessConfirmBegin')
    if request.method=='GET':
        SignNature = request.GET.get('signature',default='')
        logger.info('SignNature get is '+SignNature)
        TimeStamp = request.GET.get('timestamp',default='')
        logger.info('TimeStamp get is '+TimeStamp)
        Nonce = request.GET.get('nonce',default = '')
        logger.info('Nonce get is '+Nonce)
        EchoStr = request.GET.get('echostr',default='')
        logger.info('EchoStr get is '+EchoStr)
        if SignNature == '' or TimeStamp == '' or Nonce == '' or EchoStr == '' :
            logger.info('Confire failed wrong param!')
            return HttpResponse('wrong param!')
        Token = 'tokenofnazhefangbianmian'

        StrList = [Token,TimeStamp,Nonce]
        StrList.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,StrList)
        HashResult = sha1.hexdigest()

        if HashResult == SignNature :
            return HttpResponse(EchoStr)
        


