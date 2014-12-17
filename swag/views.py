#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.templatetags.static import static
from django.template import Template
from django.template import Context
from django.http import HttpResponse
import maps

def map_list(request):
    """ Display a list of available swagmaps """    
    map_data = maps.get_all()
    return render_to_response(
        'swag/map_list.html',
        { "maps" : map_data }
    )

def map_view(request,map_id):
    """ Display a swagmap
    
    @map_id is currently a path like `KTouch/ktouch.json`, 
    but may change to a proper DB object ID
    """
    data = maps.get_data(map_id)
    url =  maps.get_url(request,map_id)
    return render_to_response(
        'swag/map_view.html',
        {'url':url, "map":data}
    )
