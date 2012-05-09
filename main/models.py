from django.db.models import *
from django.core.urlresolvers import reverse
from datetime import *
from random import *

class Char(Model):
    char = CharField(max_length=8)
    desc = CharField(max_length=256)

    def __unicode__(self):
        return unichr(int(self.char, 16))

class DailyChar(Model):
    char = ForeignKey(Char)
    day = DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('old', None, kwargs=dict(pk=self.id))

    @staticmethod
    def current():
        #TODO: Stop this having a race condition, tralalala.
        #Uncomment the following line to get a new character each refresh.
        DailyChar.objects.filter(day=date.today()).delete()
        if DailyChar.objects.filter(day=date.today()).count() == 0:
            numChars = Char.objects.all().count()
            char = Char.objects.get(id=int(1+random()*numChars))
            DailyChar(char=char).save()
        return DailyChar.objects.get(day=date.today())


