from django.db import models

class root_admin(models.Model):
    #root超级管理员表
    id = models.AutoField(primary_key=True)
    root_name = models.CharField(verbose_name="用户名",max_length=32)
    root_passwd = models.CharField(verbose_name="密码",max_length=64)

class userinfo(models.Model):
    #普通用户表
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32,verbose_name="普通用户名")
    user_passwd = models.CharField(max_length=64,verbose_name="普通密码")

class cat(models.Model):
    #一级目录
    id = models.AutoField(primary_key=True)
    cat = models.CharField(verbose_name="一级目录",max_length=255)

class subcat(models.Model):
    #二级目录
    id = models.AutoField(primary_key=True)
    subcatname = models.CharField(verbose_name="二级目录",max_length=255)
    sub_cat = models.ForeignKey(to="cat",to_field='id',default=1,on_delete=models.CASCADE)

class link(models.Model):
    #站点的详细信息
    id = models.AutoField(primary_key=True)
    web_name = models.CharField(verbose_name="站点名称",max_length=255)
    web_info = models.CharField(verbose_name="站点信息",max_length=1024)
    web_url = models.URLField(verbose_name="站点url",max_length=255)
    url_num = models.IntegerField(verbose_name="访问数量",default=0)
    web_type = models.ForeignKey(to="subcat",to_field='id',default=1,on_delete=models.CASCADE)


class error(models.Model):
    #错误的站点
    id = models.AutoField(primary_key=True)
    err_web = models.ForeignKey(to="link",to_field='id',default=1,on_delete=models.CASCADE)



# Create your models here.
