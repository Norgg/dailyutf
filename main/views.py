from django.views.generic import *
from django.contrib.syndication.views import Feed
from models import *
from datetime import *
from random import *

class Main(DetailView):
    template_name = "main.html"
    
    def get_object(queryset=None):
        #Uncomment the following line to get a new character each refresh.
        DailyChar.objects.filter(day=date.today()).delete()
        if DailyChar.objects.filter(day=date.today()).count() == 0:
            numChars = Char.objects.all().count()
            char = Char.objects.get(id=int(1+random()*numChars))
            DailyChar(char=char).save()
        return DailyChar.objects.get(day=date.today())

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
        return unicode("<p>" + item.char.desc + "<br/>" + unichr(int(item.char.char, 16)) + "</p>")
