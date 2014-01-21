from calendario.models import *
from common.response import JSONResponse
from common.utils import qdct_as_kwargs
from django.http import HttpResponse
from django.template import RequestContext, loader
import time
#from django.contrib.auth.decorators import login_required


mnames = "January February March April May June July August September October November December"
mnames = mnames.split()


#@login_required
def main(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year, year+1, year+2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # are there entry(s) for this month; current month?
            entries = Event.objects.filter(start__year=y, start__month=n+1)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
        lst.append((y, mlst))
        
    context = RequestContext(request, {
        'modulo': 'Calendario',                               
        'years': lst,
        'user': request.user,
        'year': year,
    })    
    template = loader.get_template('calendario.html')    
    return HttpResponse(template.render(context));

  
def json_get_events(request):
 
    #if not request.method == "POST":
        # return all cities if any filter was send
    #   return JSONResponse(Event.objects.order_by('start'))
 
    # get cities with request.POST as filter arguments
    events = Event.objects.filter(**qdct_as_kwargs(request.POST)).order_by('start')
 
    #return JSONResponse with id and name
    return JSONResponse(events.values('id','title','start','end'))