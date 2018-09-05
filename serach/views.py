from django.shortcuts import render,HttpResponse,redirect
from serach import models



#管理员登录验证装饰器
def auth(func):
    def inner(request,*args,**kwargs):
        # ck = request.session.get("is_login",None)
        #   request.session.get("username")用户信息
        ck = models.root_admin.objects.filter(root_name=request.session.get("username")).first()
        if ck == None:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner

#用户登录验证装饰器
def auth_user(func):
    def inner_user(request,*args,**kwargs):
        # ck = request.session.get("is_login",None)
        #   request.session.get("username")用户信息
        ck = models.userinfo.objects.filter(user_name=request.session.get("username")).first()
        if ck == None:
            return redirect('/index/')
        return func(request,*args,**kwargs)
    return inner_user

@auth
def admin(request):
    #管理员后台  创建一级目录
    # user = request.session.get("username")
    # obj = models.root_admin.objects.all()
    if request.method == "GET":
        return redirect("/add_cat1/")
    else:
        return redirect("/index/")


@auth
def add_cat1(request):
    #添加一级目录表
    # obj = models.root_admin.objects.all()
    obj_cat_info = models.cat.objects.all()
    if request.method == "POST":
        obj_cat_1 = request.POST.get("cat_1")
        if models.cat.objects.filter(cat=obj_cat_1).first():
            user_list = models.cat.objects.filter().all()
            obj_info = "该目录以存在"
            return render(request, "add_cat1.html",
                          {"obj_info": obj_info, "user_list": user_list, 'obj': request.session.get("username"),"obj_cat_info": obj_cat_info})
        models.cat.objects.create(cat=obj_cat_1).save()
        if models.cat.objects.filter(cat=obj_cat_1).first():
            obj_info = "创建成功"
        else:
            obj_info = "创建失败"
        user_list = models.cat.objects.filter().all()
        return render(request,"add_cat1.html",{"obj_info":obj_info,"user_list":user_list,'obj':request.session.get("username"),"obj_cat_info":obj_cat_info})
    elif request.method == "GET":
        #获取一级目录
        user_list = models.cat.objects.filter().all()
        return render(request, "add_cat1.html", {"user_list": user_list,'obj':request.session.get("username"),"obj_cat_info":obj_cat_info})

@auth
def cat1_del(request,nid):
    #删除一级目录
    # obj = models.root_admin.objects.all()
    models.cat.objects.filter(id=nid).delete()
    user_list = models.cat.objects.filter().all()
    num = models.cat.objects.all().count()
    return render(request, "add_cat1.html", {"user_list": user_list,
                                             'obj':request.session.get("username")})

@auth
def add_cat2(request):
    # 添加二级目录表
    # obj = models.root_admin.objects.all()    #获取管理员信息
    num = models.subcat.objects.all().count()
    if request.method == "POST":
        obj_cat_2 = request.POST.get("cat_2")   #从前端获取值
        cat_id = int(request.POST.get("cat1_id"))
        if models.subcat.objects.filter(subcatname=obj_cat_2).first():#判断目录是否存在
            user_list = models.cat.objects.all()
            obj_1 = models.subcat.objects.all()
            obj_info = "该目录以存在"
            return render(request, "add_cat2.html",
                          {"user_list": user_list, "obj_1": obj_1, "obj_info": obj_info,
                           'obj': request.session.get("username")})
        models.subcat.objects.create(subcatname=obj_cat_2,sub_cat_id=cat_id).save() #写入数据库
        if models.subcat.objects.filter(subcatname=obj_cat_2).first():  #判断数据是否写入
            obj_info = "创建成功"
        else:
            obj_info = "创建失败"
        user_list = models.cat.objects.all()  # 获取一级目录
        obj_1 = models.subcat.objects.all()    #获取数据库数据   写到前端
        return render(request, "add_cat2.html",
                      {"user_list": user_list, "obj_1": obj_1,"obj_info":obj_info,
                       'obj':request.session.get("username")})
    elif request.method == "GET":
        # 获取一二级目录
        user_list = models.cat.objects.all()
        obj_1 = models.subcat.objects.all()  # 获取二级目录
        return render(request, "add_cat2.html",
                      {"user_list": user_list, "obj_1":obj_1,
                       'obj':request.session.get("username")})
@auth
def cat2_del(request,nid):
    #删除二级目录
    # obj = models.root_admin.objects.all()
    num = models.subcat.objects.all().count()
    models.subcat.objects.filter(id=nid).delete()
    user_list = models.cat.objects.all()
    obj_1 = models.subcat.objects.all()  # 获取二级目录
    return render(request, "add_cat2.html",
                  {"user_list": user_list, "obj_1": obj_1,
                   'obj':request.session.get("username")})
@auth
def add_web(request):
    #创建站点
    # obj = models.root_admin.objects.all()  # 获取管理员信息
    if request.method == "POST":
        obj_cat_name = request.POST.get("web_name")  # 获取站点名称
        obj_cat_info = request.POST.get("web_info")  # 获取站点信息
        obj_cat_url = request.POST.get("web_url")  # 获取站点url
        cat_id_2 = int(request.POST.get("web_id_2"))  # 从选择框第二级中获取数据
        if models.link.objects.filter(web_name=obj_cat_name).first():  # 判断站点是否存在
            obj_info = "该站点以存在"
            user_list = models.cat.objects.all()
            obj_1 = models.subcat.objects.all()  # 获取二级目录
            obj_2 = models.link.objects.all()  # 获取站点信息
            return render(request, "add_web.html",
                          {"user_list": user_list, "obj_1": obj_1,  # 一二级目录
                           "obj_2": obj_2, "obj_info": obj_info,  # 站点信息
                           'obj': request.session.get("username")})  # 管理员信息
        models.link.objects.create(web_name=obj_cat_name,
                                   web_info=obj_cat_info,
                                   web_url=obj_cat_url,
                                   web_type_id=cat_id_2)  # 写入数据库
        if models.link.objects.filter(web_name=obj_cat_name).first():  # 判断数据是否写入
            obj_info = "创建成功"
        else:
            obj_info = "创建失败"
        user_list = models.cat.objects.all()
        obj_1 = models.subcat.objects.all()  # 获取二级目录
        obj_2 = models.link.objects.all()   #获取站点信息
        return render(request, "add_web.html",
                      { "user_list":user_list,"obj_1": obj_1,                 #一二级目录
                       "obj_2":obj_2,"obj_info":obj_info,                                           #站点信息
                       'obj':request.session.get("username")})#管理员信息

    elif request.method == "GET":
        # 获取站点信息
        user_list = models.cat.objects.all()
        obj_1 = models.subcat.objects.all()  # 获取二级目录
        obj_2 = models.link.objects.all()  # 获取站点信息
        return render(request, "add_web.html",
                      {"user_list":user_list,"obj_1": obj_1,  # 一二级目录
                       "obj_2": obj_2,  # 站点信息
                       'obj':request.session.get("username")})  # 管理员信息

@auth
def add_web_del(request,nid):
    #删除站点
    # obj = models.root_admin.objects.all()
    models.link.objects.filter(id=nid).delete()
    user_list = models.cat.objects.all()  # 获取一级目录
    obj_1 = models.subcat.objects.all()  # 获取二级目录
    obj_2 = models.link.objects.all()  # 获取站点信息
    return render(request, "add_web.html",
                  {"user_list": user_list, "obj_1": obj_1,  # 一二级目录
                   "obj_2": obj_2,  # 站点信息
                   'obj':request.session.get("username")})  # 管理员信息

@auth
def web_error(request):
    #查看出错站点
    # obj = models.root_admin.objects.all()
    if request.method == "GET":
        link_error = models.error.objects.all()
        link_error_link = models.link.objects.all()
        return render(request, "web_error.html", {'link_error_link':link_error_link,'link_error':link_error,
                                                    'obj':request.session.get("username")})
    elif request.method == "POST":
        models.error.objects.all().delete()
        link_error = models.error.objects.all()
        link_error_link = models.link.objects.all()
        return render(request, "web_error.html", {'link_error_link': link_error_link, 'link_error': link_error,
                                                  'obj':request.session.get("username")})
@auth
def web_err_del(request,nid):#删除出错站点
    # obj = models.root_admin.objects.all()
    models.link.objects.filter(id=nid).delete()
    link_error = models.error.objects.all()
    link_error_link = models.link.objects.all()
    return render(request, "web_error.html", {'link_error_link': link_error_link, 'link_error': link_error,
                                              'obj':request.session.get("username")})

def register(request):
    #注册
    if request.method == "GET":
        return render(request, "register.html", {"obj_error": "提交"})
    elif request.method == "POST":
        username = request.POST.get("user")
        passwd = request.POST.get("pwd")
        if models.userinfo.objects.filter(user_name=username).first():
            return render(request, "register.html",{"obj_error":"该用户存在"})
        obj = userinfo.objects.create(user_name=username,user_passwd=passwd)
        obj.save()
        return render(request,"login.html")
    else:
        return HttpResponse("error")

# @auth
def login(request):
    #登录页面
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        name = request.POST.get("user")
        pwd = request.POST.get("pwd")
        obj_root = models.root_admin.objects.filter(root_name=name,root_passwd=pwd).first()
        obj = models.userinfo.objects.filter(user_name=name,user_passwd=pwd).first()
        if obj_root:
            request.session['username'] = name  # 在session设置值
            request.session['is_login'] = True
            return redirect("/add_cat1/")
        elif obj:
            request.session['username'] = name  # 在session设置值
            request.session['is_login'] = True
            return redirect("/user_add_web/")
        else:
            return render(request, "login.html")


def login_del(request):
    #用户退出登录
    if request.method == "GET":
        request.session.clear()
        return redirect("/index/")
    else:
        request.session.clear()
        return redirect("/index/")
# del request.session['username']   删除session
    # request.session.clear()  清空session

def index(request):#主页
    obj = models.cat.objects.all()
    obj1 = models.subcat.objects.all()
    obj2 = models.link.objects.all()
    return render(request, "index.html", {'obj': obj, 'obj1': obj1, 'obj2': obj2})

def search_cat2(request,nid):
    #查看二级某一项的三级站点
    obj_cat2_link = models.link.objects.filter(web_type_id=nid).all()
    return render(request,"search_cat2.html",{"obj2_cat_link":obj_cat2_link})



def search(request):
    #搜索页面
    if request.method == "GET":
        return redirect('/index/')
    elif request.method == "POST":
        obj = request.POST.get("search_key_name")
        obj1 = models.link.objects.filter(web_name__icontains=obj).all()   #进行忽略大小写 like '%aaa%'
        obj2 = models.link.objects.filter(web_info__icontains=obj).all()
        if not (obj1 or obj2):
            url = "https://www.baidu.com/s?ie=utf-8dg&wd=" + str(obj)
            return redirect(url)
        array1=[]
        array = []
        for i in obj1:
            array1.append(i)
        for j in obj2:
            array1.append(j)
        for i in array1:
            if (i not in array):
                array.append(i)
        return render(request,"search.html",{"obj":obj,
                                             "obj1":array
                                             })

@auth_user
def user_add_web(request):
    #用户添加站点信息
    if request.method == "POST":
        obj_cat_name = request.POST.get("web_name")  # 获取站点名称
        obj_cat_info = request.POST.get("web_info")  # 获取站点信息
        obj_cat_url = request.POST.get("web_url")  # 获取站点url
        cat_id_2 = int(request.POST.get("web_id_2"))  # 从选择框第二级中获取数据
        if models.link.objects.filter(web_name=obj_cat_name).first():  # 判断站点是否存在
            obj_info = "该站点以存在"
            user_list = models.cat.objects.all()
            obj_1 = models.subcat.objects.all()  # 获取二级目录
            obj_2 = models.link.objects.all()  # 获取站点信息
            return render(request, "user_add_web.html",
                          {"user_list": user_list, "obj_1": obj_1,  # 一二级目录
                           "obj_2": obj_2, "obj_info": obj_info,  # 站点信息
                           'obj': request.session.get("username")})  # 管理员信息
        models.link.objects.create(web_name=obj_cat_name,
                                   web_info=obj_cat_info,
                                   web_url=obj_cat_url,
                                   web_type_id=cat_id_2)  # 写入数据库
        if models.link.objects.filter(web_name=obj_cat_name).first():  # 判断数据是否写入
            obj_info = "创建成功"
        else:
            obj_info = "创建失败"
        user_list = models.cat.objects.all()
        obj_1 = models.subcat.objects.all()  # 获取二级目录
        obj_2 = models.link.objects.all()  # 获取站点信息
        return render(request, "user_add_web.html",
                      {"user_list": user_list, "obj_1": obj_1,  # 一二级目录
                       "obj_2": obj_2, "obj_info": obj_info,  # 站点信息
                       'obj': request.session.get("username")})  # 管理员信息

    elif request.method == "GET":
        # 获取站点信息
        user_list = models.cat.objects.all()
        obj_1 = models.subcat.objects.all()  # 获取二级目录
        obj_2 = models.link.objects.all()  # 获取站点信息
        return render(request, "user_add_web.html",
                      {"user_list": user_list, "obj_1": obj_1,  # 一二级目录
                       "obj_2": obj_2,  # 站点信息
                       'obj': request.session.get("username")})  # 管理员信息


def info_error(request,nid):
    if request.method == "GET":
        if models.error.objects.filter(err_web_id=nid):
            obj_err = "此错误以被提交"
        else:
            models.error.objects.create(err_web_id=nid)
            obj_err = "错误提交成功"
        return render(request,"link_error.html",{"obj_err":obj_err})





# Create your views here.
