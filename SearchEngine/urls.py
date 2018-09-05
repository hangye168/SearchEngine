"""SearchEngine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from serach import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.index),
    url('^admin/$', views.admin),
    url('^index/$', views.index),#主页
    url('^login/$', views.login),#登录
    url('^register/$', views.register),#注册
    url('^cat1_del-(?P<nid>\d+)/$', views.cat1_del),#删除一级目录
    url('^add_cat1/$', views.add_cat1),#创建一级目录
    url('^add_cat2/$', views.add_cat2),#创建二级目录
    url('^cat2_del-(?P<nid>\d+)/$', views.cat2_del),#删除二级目录
    url('^add_web/$', views.add_web),  # 创建站点
    url('^add_web_del-(?P<nid>\d+)/$', views.add_web_del),  # 删除站点
    url('^web_error/$', views.web_error),  # 访问出错站点
    url('^web_err_del-(?P<nid>\d+)/$', views.web_err_del),  # 删除出错站点
    url('^search/$', views.search),  # 搜索页面
    url('^search_cat2-(?P<nid>\d+)/$', views.search_cat2),  #用二级目录查三级目录
    url('^login_del/$', views.login_del),#退出
    url('^user_add_web/$', views.user_add_web),#用户添加
    url('^info_error-(?P<nid>\d+)/$', views.info_error),#用户报错
    # url('^userdetail-(?P<nid>\d+)/', views.user_detail),

]
