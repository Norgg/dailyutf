from django.db.models import *
from django.core.urlresolvers import reverse

class Char(Model):
    char = CharField(max_length=8)
    desc = CharField(max_length=256)

class DailyChar(Model):
    char = ForeignKey(Char)
    day = DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('old', None, kwargs=dict(pk=self.id))
