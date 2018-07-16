from django.db import models
class BaseModel(models.Model):
    # 数据创建时间自动赋值
    add_date = models.DateTimeField(auto_now_add=True)
    # 数据的修改时间，自动赋值
    update_date = models.DateTimeField(auto_now=True)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    class Meta:
        abstract=True