from django.db import models


# Create your models here.
# default create table name appname_classname eg:cmdb_server
class Server(models.Model):
    """服务器设备"""
    server_type_choice = ((0, 'PC服务器'),
                          (1, '刀片机'),
                          (2, '小型机'),
                          )
    add_type_choice = (('auto', '自动添加'),
                       ('manual', '手工录入'),
                       )
    asset_type = models.SmallIntegerField(choices=server_type_choice, default=0, verbose_name="服务器类型")
    add_type = models.CharField(choices=add_type_choice, max_length=32, default='auto', verbose_name="添加方式")
    hosted_on = models.ForeignKey('self', related_name='hosted_on_server', blank=True, null=True, verbose_name="宿主机",
                                  on_delete=models.CASCADE)
    # 虚拟机专用字段
    IP = models.CharField('IP地址', max_length=30, default='')
    MAC = models.CharField('Mac地址', max_length=200, default='')
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    hostname = models.CharField(max_length=128, null=True, blank=True, verbose_name="主机名")
    os_type = models.CharField('操作系统类型', max_length=64, blank=True, null=True)
    os_distribution = models.CharField('发行商', max_length=64, blank=True, null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"
