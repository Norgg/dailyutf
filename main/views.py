from django.views.generic import *
from models import *
from datetime import *
from random import *

class Main(DetailView):
  def get_object(queryset=None):
    
    #Uncomment the following line to get a new character each refresh.
    #DailyChar.objects.filter(day=date.today()).delete()
    if DailyChar.objects.filter(day=date.today()).count() == 0:
      numChars = Char.objects.all().count()
      char = Char.objects.get(id=int(1+random()*numChars))
      DailyChar(char=char).save()
    return DailyChar.objects.get(day=date.today())
  template_name = "main.html"
