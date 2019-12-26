# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.author
