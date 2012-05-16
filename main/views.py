from django.views.generic import *
from django.contrib.syndication.views import Feed
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from datetime import *

from models import *

class Main(DetailView):
    template_name = "main.html"
    
    def get_object(queryset=None):
        return DailyChar.current()

    def get_context_data(self, **kwargs):
        ctx = super(Main, self).get_context_data(**kwargs)
        sess = self.request.session
        if sess.has_key('voted'):
            if sess['voted'] == date.today() and sess.has_key('voted_for'):
                try:
                    ctx['voted_for'] = NextCharVotes.objects.get(id=sess['voted_for'])
                except NextCharVotes.DoesNotExist:
                    ctx['candidates'] = NextCharVotes.objects.all()[0:5]
            else:
                ctx['candidates'] = NextCharVotes.objects.all()[0:5]
        else:
            ctx['candidates'] = NextCharVotes.objects.all()[0:5]
        return ctx

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
        return unicode("<p>%s<br/>%s</p><p>Vote for the next character <a href='http://thedailyutf.com'>here</a>.</p>" % (item.char.desc,item.char))

def json(request):
    item = DailyChar.current()
    char_json = simplejson.dumps(dict(d=item.char.desc, c=unicode(item.char)))
    return HttpResponse(char_json, mimetype='application/json')

def vote(request, pk=None):
    if not request.session.has_key('voted') or request.session['voted'] != date.today():
        try:
            candidate = NextCharVotes.objects.get(id=pk)
            candidate.votes += 1
            candidate.save()
            request.session['voted'] = date.today()
            request.session['voted_for'] = pk
        except NextCharVotes.DoesNotExist:
            pass
    return redirect(reverse('home'))
