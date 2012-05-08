from django.db.models import *

class Char(Model):
  char = CharField(max_length=8)
  desc = CharField(max_length=256)

class DailyChar(Model):
  char = ForeignKey(Char)
  day = DateField(auto_now_add=True)
