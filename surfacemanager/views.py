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

# def test(request):
#     with open("templates/publications.txt",encoding="utf-8") as f:
#         line = f.readline()
#         while line:
#             pb = [i.strip() for i in line.split("@")]
#             print(pb)
#             qulist = Publication()
#             qulist.author = pb[0]
#             qulist.paper_title = pb[1]
#             qulist.conference = pb[2]
#             qulist.save()
#             line = f.readline()
#     return JsonResponse({"mes":"ok"})



# def test2(request):
#     from lxml import etree
#     ht = """
#     <div class="container">
#         <div class="row">
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/zhaopinlogo.jpg" class="project-logo"/>
#                         <p class="project-name">招聘知识图谱</p>
#                         <p class="project-description">
#                             采集求职领域人物/公司/职位信息，抽取个人技能与业务要求，细化领域schema，构建职业知识图谱，进一步支持基于知识图谱的问答搜索与精准推荐应用（数据来源：智联招聘）
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#                                 <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8003')">内网入口</button>
#                             </div>
#                             <div class="col-6">
#                                 <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://zhaopin.demo.actkg.com')">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/ddlogo.jpg" class="project-logo"/>
#                         <p class="project-name">导弹知识图谱</p>
#                         <p class="project-description">
#                             采集世界导弹大全电子书上的导弹资料，整理结构信息，规范属性体系，补全领域实体，构建领域图谱，支撑导弹相关知识的检索与问答应用（数据来源：世界导弹大全）
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#                                 <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8004')">内网入口</button>
#                             </div>
#                             <div class="col-6">
#                                 <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://dd.demo.actkg.com')">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/banklogo.png" class="project-logo"/>
#                         <p class="project-name">银行知识图谱</p>
#                         <p class="project-description">
#                             采集银行法规条款以及业务说明文档，设计业务图谱schema，基于文本抽取知识，构建银行图谱，支撑银行内部业务领域内的问答与检索（数据来源：工商银行网站法规条例与业务说明）
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#                                 <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8002')">内网入口</button>
#                             </div>
#                             <div class="col-6">
#                                 <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://icbc.demo.actkg.com')">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/gamelogo.png" class="project-logo"/>
#                         <p class="project-name">游戏知识图谱</p>
#                         <p class="project-description">
#                             自各大游戏网站采集各类单机游戏、游戏公司、游戏玩家等相关数据，建立游戏分类与标签体系，识别实体并建立实体间关联，构建游戏图谱，支撑游戏业务领域内的问答与推荐（数据来源：Steam等游戏网站）
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#                                 <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8010')">内网入口</button>
#                             </div>
#                             <div class="col-6">
#                                 <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://youxi.demo.actkg.com')">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/medlog.jpg" class="project-logo"/>
#                         <p class="project-name">病理知识图谱</p>
#                         <p class="project-description">
#                             通过医疗检验单，推断病人可能患有的患病，并给出原因。
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#                                 <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8021')">内网入口</button>
#                             </div>
#                             <div class="col-6">
#                                 <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://med.demo.actkg.com')">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/medlog.jpg" class="project-logo"/>
#                         <p class="project-name">科技人才知识图谱</p>
#                         <p class="project-description">
#                             汇聚科技人才大数据资源，建设数据规范、结构完整、支撑有力的科技人才数据服务平台
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#                                 <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8090')">内网入口</button>
#                             </div>
#                             <div class="col-6">
#                                 <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://ep.demo.actkg.com')">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/1.jfif" class="project-logo"/>
#                         <p class="project-name">唐诗知识图谱</p>
#                         <p class="project-description">
#                             采用知识抽取、知识融合、知识推理等技术构建唐诗知识图谱,统一表示和组织唐诗领域数据,实现对大规模唐诗数据的语义化处理，将诗人、诗歌、意象、情感等常见诗歌元素融为一体，支撑唐诗相关知识的检索与问答应用，为用户提供一个直观化的古典文化学习与展示平台（数据来源：百度百科、维基百科）
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#     <!--                            <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8090')">内网入口</button>-->
#                                 <button class="btn btn-inverse btn-block" type="button">内网入口</button>
#                             </div>
#                             <div class="col-6">
#     <!--                            <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://ep.demo.actkg.com')">外网入口</button>-->
#                                 <button class="btn btn-primary btn-block" type="button">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/3.jpg" class="project-logo"/>
#                         <p class="project-name">科普资源知识图谱</p>
#                         <p class="project-description">
#                             融合了科普资讯，科普展品，科普语音视频等多模态科普资源，将不同形态，不同领域的知识内容联系并整合在一起，为打造上层科普资源知识图谱的应用场景提供有力保障
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#     <!--                            <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8090')">内网入口</button>-->
#                                 <button class="btn btn-inverse btn-block" type="button">内网入口</button>
#                             </div>
#                             <div class="col-6">
#     <!--                            <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://ep.demo.actkg.com')">外网入口</button>-->
#                                 <button class="btn btn-primary btn-block" type="button">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#             <div class="col-12 col-lg-4 mb-4">
#                 <div class="card">
#                     <div class="card-body">
#                         <img src="/static/img/logos/2.jpg" class="project-logo"/>
#                         <p class="project-name">产业知识图谱</p>
#                         <p class="project-description">
#
#                         </p>
#                         <div class="row pt-4">
#                             <div class="col-6">
#     <!--                            <button class="btn btn-inverse btn-block" type="button" onclick="window.open('http://10.1.1.28:8090')">内网入口</button>-->
#                                 <button class="btn btn-inverse btn-block" type="button">内网入口</button>
#                             </div>
#                             <div class="col-6">
#     <!--                            <button class="btn btn-primary btn-block" type="button" onclick="window.open('http://ep.demo.actkg.com')">外网入口</button>-->
#                                 <button class="btn btn-primary btn-block" type="button">外网入口</button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#         </div>
#     </div>
#     """
#     html = etree.HTML(ht)
#     project_ico = html.xpath("//div[@class='card']//img")
#     project_name = html.xpath("//p[@class='project-name']/text()")
#     project_description = html.xpath("//p[@class='project-description']/text()")
#     url_outer = html.xpath("//div[contains(@class,'row pt-4')]/div[position()=1]/button")
#     url_in = html.xpath("//div[contains(@class,'row pt-4')]/div[position()=2]/button")
#
#     for i in range(0, len(project_ico)):
#         print(project_ico[i].get("src").strip())
#         print(project_name[i].strip())
#         print(project_description[i].strip())
#         dem = Democard()
#         dem.project_ico = project_ico[i].get("src").strip()
#         dem.project_name = project_name[i].strip()
#         dem.project_description = project_description[i].strip()
#         if i<len(url_outer):
#             if url_outer[i].get("onclick"):
#                 print(url_outer[i].get("onclick").strip()[13:-2])
#                 print(url_in[i].get("onclick").strip()[13:-2])
#                 dem.url_outer = url_outer[i].get("onclick").strip()[13:-2]
#                 dem.url_intranet = url_in[i].get("onclick").strip()[13:-2]
#             else:
#                 print("{} {}".format(url_outer[i].get("onclick"),i))
#         print("- "*10)
#         dem.save()
#     return JsonResponse({"ok":"ok"})


