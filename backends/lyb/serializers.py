# -*- coding: utf-8 -*-
# @Author: wei
# @Date: 2024年02月21日
# @Env: python 3.8.10
# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Lyb

#  序列化器
class LybSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyb
        # 序列化所有字段
        fields = "__all__"
