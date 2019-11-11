from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from utils import jsonify
from .models import Publication,Democard

class Publications(View):

    def get(self,request):
        questlist = Publication.object.all()
        return JsonResponse(jsonify(questlist,allow=["id","author","paper_title","conference"]),status=200)

class Demos(View):
    def get(self,request):
        questlist = Democard.object.all()
        return JsonResponse(jsonify(questlist))

def test(request):
    with open("templates/publications.txt",encoding="utf-8") as f:
        line = f.readline()
        while line:
            pb = [i.strip() for i in line.split("@")]
            print(pb)
            qulist = Publication()
            qulist.author = pb[0]
            qulist.paper_title = pb[1]
            qulist.conference = pb[2]
            qulist.save()
            line = f.readline()
    return JsonResponse({"mes":"ok"})



