from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
    }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'firstname': 'Linus',  
    'mymembers': mymembers, 
    'greeting': 1, 
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
    'cars': [{"brand": "Ford", "model": "Mustang", "year": 2022}, 
            {"brand": "Toyota", "model": "Corolla", "year": 2000},{"brand":"Banana", "model": "Apple", "year": 2015}]

  


  }
  return HttpResponse(template.render(context, request))