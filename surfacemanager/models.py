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


