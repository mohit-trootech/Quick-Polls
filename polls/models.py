# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
import datetime
from django.utils.html import format_html
from polls.constants import (
    THUMBNAIL_PREVIEW_HTML,
    THUMBNAIL_PREVIEW_TAG,
    QUESTION_MEDIA_PATH,
    QUESTION_TAG_DEFAULT,
    QUESTION_TAG_RELATED_NAME,
    CHOICE_QUESTION_RELATED_NAME,
)


class Tag(TitleDescriptionModel):

    def __str__(self):
        return self.title

    class meta:
        ordering = ["title"]


class Question(TitleDescriptionModel, TimeStampedModel):

    total_votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to=QUESTION_MEDIA_PATH, blank=True, null=True)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name=QUESTION_TAG_RELATED_NAME,
        default=QUESTION_TAG_DEFAULT,
    )

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now

    @property
    def thumbnail_preview(self):
        if self.image:
            return format_html(THUMBNAIL_PREVIEW_TAG.format(self.image.url))
        return format_html(THUMBNAIL_PREVIEW_HTML)


class Choice(TitleDescriptionModel, TimeStampedModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name=CHOICE_QUESTION_RELATED_NAME
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class meta:
        ordering = ["title"]
