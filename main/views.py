from django.views.generic import *
from django.contrib.syndication.views import Feed
from django.http import HttpResponse
from django.utils import simplejson
from models import *

class Main(DetailView):
    template_name = "main.html"
    
    def get_object(queryset=None):
        return DailyChar.current()

class Random(DetailView):
    template_name = "main.html"
    
    def get_object(queryset=None):
        return DailyChar.random()

class Old(DetailView):
    template_name = "main.html"
    model = DailyChar

class CharFeed(Feed):
    title = "The Daily UTF Feed"
    link = "/feed"
    description = "Every UTF"

    def items(self):
        return DailyChar.objects.order_by('-day')[:10]

    def item_title(self, item):
        return item.char.desc

    def item_description(self, item):
        return unicode("<p>%s<br/>%s</p>" % (item.char.desc,item.char))

def json(request):
    item = DailyChar.current()
    char_json = simplejson.dumps(dict(d=item.char.desc, c=unicode(item.char)))
    return HttpResponse(char_json, mimetype='application/json')
