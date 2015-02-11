from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from urllib import urlopen
import json

# TODO: this should be dynamically configurable!
# Set to None to return an empty dummy response
# instead of trying to access a real LRS
#XAPI_URL = None
XAPI_URL = "http://staging.tunapanda.org/learninglocker.git/public/data/xAPI/"

def dummy_response(request):
    res = json.dumps({"statements":[]})
    return HttpResponse(res, content_type="text/javascript")

def main(request,path="WTF"):
    if XAPI_URL is None:
        return dummy_response(request)
    url = XAPI_URL + path + "?" + request.META['QUERY_STRING']
    print "XXX URL: %s" % url
    url_data = urlopen(url)
    res = url_data.read()
    print "XXX RES %s\n%s" % res
    return HttpResponse(res, content_type="text/javascript")
    
    
    
