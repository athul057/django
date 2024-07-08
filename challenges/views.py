from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string;

# Create your views here.
plans={
 "jan":"hi jan",
 "feb":"hi feb",
 "mar":"hi mar",
 "apr":"hi apr",
 "may":"hi may",
 "june":"hi june",
 "july":"hi july",
 "aug":"hi aug",
 "sep":"hi sep",
 "oct":"hi oct",
 "nov":"hi nov",
 "dec":"hi dec",
}


# def main(request,mont):
#  context=None
#  month=mont.lower()
#  if(month=="january"):
#   context="Hi jan"
#  elif(month=="feb"):
#   context="Hi Fex"
#  elif(month=="march"):
#   context="Hi March"
#  else:
#   return HttpResponseNotFound("Something happend")
#  return HttpResponse(context)

# def index(request):
#  items=list(plans.keys())
#  list_items=""
 
#  for item in items:
#   my_link=reverse("mon",args=[item])
#   list_items+=f"<li><a href=\"{my_link}\">{item.capitalize()}</a></li>"
#  response_data=f"<ul>{list_items}</ul>"
#  return HttpResponse(response_data)



def index(request):
 return render(request,'challenges/index.html',{
  'months':plans
 })


def month(request,myMonth):
 try:
  # return HttpResponse(plans[myMonth])
  # return HttpResponse(render_to_string('challenges/challenge.html'))
  return render(request,'challenges/challenge.html',{
   'text':plans[myMonth],'month':myMonth
  })
 except:
  return HttpResponseNotFound("Errorr...")



def monthNum(request,myMonth):

 m=list(plans.keys())
 myVal=m[myMonth-1]
#  return HttpResponseRedirect("/challenges/"+myVal)
 redirect_path=reverse("mon",args=[myVal])
 return HttpResponseRedirect(redirect_path)

