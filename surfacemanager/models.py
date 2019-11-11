from django.db import models

# Create your models here.

class Publication(models.Model):
    class Meta:
        db_table = 'publication'
        verbose_name = verbose_name_plural = "publications"

    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, null=True,verbose_name="作者")
    paper_title = models.CharField(max_length=200,null=True,verbose_name="论文名称")
    conference = models.CharField(max_length=50,null=True,verbose_name="会议/期刊")

    def __repr__(self):
        return "<Publication {} {} {} {}>".format(
            self.id, self.author, self.paper_title, self.conference
        )

    __str__ = __repr__


class Democard(models.Model):
    class Meta:
        db_table = 'zx_democard'
        verbose_name = verbose_name_plural = "Democard"

    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, null=True,verbose_name="项目名称")
    project_ico = models.CharField(max_length=80,null=True,verbose_name="图标链接")
    project_description = models.CharField(max_length=200,null=True,verbose_name="项目介绍")
    url_outer = models.CharField(max_length=50,null=True,verbose_name="外网入口")
    url_intranet = models.CharField(max_length=50, null=True, verbose_name="内网入口")


    def __repr__(self):
        return "<Democard {} {} {} {} {}>".format(
            self.id, self.project_name, self.project_description, self.url_outer,self.url_intranet
        )

    __str__ = __repr__

