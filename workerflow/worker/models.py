from django.db import models

# Create your models here.

class Worker(models.Model):
    """docstring for Worker"""
    class Meta:
        verbose_name = "人員"
    name = models.CharField("姓名", max_length=10)
    location = models.CharField("單位", max_length=60)
    title = models.CharField("職稱", max_length=20)


class Event(models.Model):
    """docstring for Event"""
    class Meta:
        verbose_name = "事件"
    name = models.CharField("姓名", max_length=10)
    # ex: new, goto, goout, gonowhere, ...
    event_type = models.CharField("事件類型", max_length=10)
    create_time = models.DatetimeField("建立時間", auto_now_add=True)
    modify_time = models.DatetimeField("修改時間", auto_now=True)
    effective_date = models.DateField("生效日期")

    date = models.DateField("發文日期", blank=True)
    # ex: xxx-字第-{number}-號
    number = models.CharField("發文字號", max_length=30, blank=True)
    # ex: {first}-{second}-{third}
    old_location = models.CharField("原單位", max_length=60, blank=True)
    old_title = models.CharField("原職稱", max_length=20, blank=True)
    new_location = models.CharField("新單位", max_length=60, blank=True)
    new_title = models.CharField("新職稱", max_length=20, blank=True)


class SystemUser(models.Model):
    """docstring for SystemUser"""
    class Meta:
        verbose_name = "系統使用人員"
    system_type = models.CharField("系統種類", max_length=10)
    name = models.CharField("姓名", max_length=10)


class SystemAdmin(models.Model):
    """docstring for SystemAdmin"""
    class Meta:
        verbose_name = "系統管理人員"
    system_type = models.CharField("系統種類", max_length=10)
    name = models.CharField("姓名", max_length=10)


class EventRecord(models.Model):
    """docstring for EventRecord"""
    class Meta:
        verbose_name = "操作紀錄"
    time = models.DatetimeField("時間", auto_now_add=True)
    name = models.CharField("姓名", max_length=10)
    event_record = models.TextField("紀錄")
