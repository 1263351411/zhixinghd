#_*_coding:utf-8_*_
from django.http import HttpResponse,JsonResponse
import simplejson
from .models import User
import jwt
import bcrypt
from django.conf import settings
from django.views import View
from utils import jsonify
import time

# 登录验证装饰器
def authenticate(viewfunc):
    def wrapper(*args):
        request = args[-1] #保证最后一个取到request对象

        # 认证越早越好
        jwtheader  = request.META.get(settings.AUTH_HEADER,"")

        if not jwtheader:
            return HttpResponse(status=401)
        print(jwtheader)
        # 解码
        try:
            payload = jwt.decode(jwtheader,settings.SECRET_KEY,algorithms=["HS256"])
            # payload = "aa"
            print(payload)
        except Exception as e: #解码有任何异常，都不能通过认证
            print(e)
            return HttpResponse(status=401)

        # 是否过期ToDO
        print("- "*30)
        try:
            user_id = payload.get("user_id",0)
            if user_id == 0:
                return HttpResponse(status=401)
            user = User.objects.get(pk=user_id)
            request.user = user
        except Exception as e:
            print(e)
            return HttpResponse(status=401)

        response = viewfunc(*args) #参数解构
        return response
    return wrapper

# 对id签名
def gen_token(user_id):
    # 时间戳用来判断是否过期，以便重发token或重新登录
    return  jwt.encode({
        "user_id":user_id,
        "exp":int(time.time()) + settings.AUTH_EXPIRE #取整
    },settings.SECRET_KEY,algorithm="HS256").decode()


class Account_Reg(View):

    # 注册接口,需要参数email，name,password
    def post(self,request):
        try:
            payload = simplejson.loads(request.body)
            print("- "*30)
            email = payload['email']
            name = payload['name']
            password = payload["password"].encode()
            print(email, name, password)

            query = User.objects.filter(email=email)
            print(query)
            print(query.query)  # 查看sQL语句
            if query.first():
                return JsonResponse({"error": "用户已存在"}, status=400)

            # 密码加密
            password = bcrypt.hashpw(password, bcrypt.gensalt()).decode()
            print(password)

            user = User()
            user.email = email
            user.name = name
            user.password = password
            user.save()

            return JsonResponse({"token": gen_token(user.id)}, status=201)  # 创建成功返回201
        except Exception as e:  # 有任何异常，都返回
            print(e)
            # 失败返回错误信息和400，所有其他错误一律用户名密码错误
            return JsonResponse({"error": "注册失败"}, status=400)


class Account_Login(View):

    def post(self,request):
        try:
            payload = simplejson.loads(request.body)
            print(payload)
            email = payload["email"]
            password = payload["password"].encode()

            user = User.objects.get(email=email)  # only one
            print(user.password)

            if bcrypt.checkpw(password, user.password.encode()):
                # 验证成功
                token = gen_token(user.id)

                res = JsonResponse({
                    "user": jsonify(user, exclude=["password"]),
                    "token": token
                })  # 返回200
                res.set_cookie("jwt", token)
                return res
            else:
                return JsonResponse({"error": "用户名或密码错误"}, status=400)
        except Exception as e:
            print(e)
            # 失败返回错误信息和400，所有其他错误一律用户名密码错误
            return JsonResponse({"error": "用户名或密码错误"}, status=400)

# @authenticate #在有需要的视图函数上加上此装饰器
# def test(request):
#     print("- "*30,"test")
#     print(request.user)
#     return JsonResponse({},status=200)


