from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.templatetags.static import static
from django.contrib.staticfiles import finders
from urllib import urlopen
import json

# TODO: Kludge. Find a better way?
static_path_prefix = "swag/maps/"

def get_all():
    # TODO: Dynamic generation. Better to use DB objects instead of files?
    map_id_list = ["KTouch/ktouch.json"]
    map_data = []
    for map_id in map_id_list:
        data = get_data(map_id)
        map_data.append({"map_id":map_id, "data":data})
    return map_data
    
    
def get_data(path):
    """Get JSON data from a path (`KTouch/ktouch.json`) or URL"""
    # Test whether we were given a full URL
    validate = URLValidator()
    try:
        validate(path)
        
    # Not a url. Treat as local file hosted by django's staticfiles system
    except ValidationError:
        path = finders.find(static_path_prefix + path)
        mapfile = open(path,"r")
        
    # URL. Get it. 
    else:
        mapfile = urlopen(path)
        
    return json.load(mapfile)
    
    
def get_url(request,path):
    """ Return a URL to wherever a map is hosted by Django's staticfiles system """
    return request.build_absolute_uri(static(static_path_prefix + path))
