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
        SignNature = request.GET.get('signature',default='52b4d31088afc0a3aeb285ca96a90925282695a6')
        logger.info('SignNature get is '+SignNature)
        TimeStamp = request.GET.get('timestamp',default='1554263502')
        logger.info('TimeStamp get is '+TimeStamp)
        Nonce = request.GET.get('nonce',default = '1480077730')
        logger.info('Nonce get is '+Nonce)
        EchoStr = request.GET.get('echostr',default='4699500745244225535')
        logger.info('EchoStr get is '+EchoStr)
        if SignNature == '' or TimeStamp == '' or Nonce == '' or EchoStr == '' :
            logger.info('Confire failed wrong param!')
            return HttpResponse('wrong param!')
        Token = 'tokenofnazhefangbianmian'

        StrList = [Token,TimeStamp,Nonce]
        StrList.sort()
        sha1 = hashlib.sha1()
        sha1.update("".join(StrList).encode("utf8"))
        HashResult = sha1.hexdigest()
        logger.info('HashResult is '+HashResult)

        if HashResult == SignNature :
            logger.info('Confirm success')
            return HttpResponse(EchoStr)
        else :
            return HttpResponse('Confirm failed')
        


