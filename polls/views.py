# -*- coding: utf-8 -*-
from django.utils import timezone
from django.views.generic import ListView, FormView, TemplateView
from polls.models import Question, Choice, Tag
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from polls.utils import (
    update_vote_data_choice_id,
)
from typing import Any
import json
from polls.forms import CreatePoll
from polls.constants import (
    HOME_TEMPLATE,
    QUESTION_CONTEXT,
    CREATE_POLLS_TEMPLATE,
    HOME_URL,
    POLLS_LIST_TEMPLATE,
    POLLS_INFO_TEMPLATE,
)


class IndexView(ListView):
    model = Question
    context_object_name = QUESTION_CONTEXT
    template_name = HOME_TEMPLATE
    paginate_by = 10

    def get_queryset(self):
        """
        return the filterd queryset

        :return:
        """
        filter_query = Q()
        orderby = self.request.GET.get("orderby", "-created")
        tag = self.request.GET.get("tag", "")
        if tag:
            filter_query = Q(tag__title=tag)

        return (
            Question.objects.prefetch_related("choice")
            .filter(Q(created__lte=timezone.now()) & filter_query)
            .order_by(orderby)
        )

    def get_template_names(self):
        """
        get template update using htmx

        :return:
        """
        if self.request.htmx:
            return POLLS_LIST_TEMPLATE
        else:
            return self.template_name

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


def vote(request) -> JsonResponse:
    """
    handles the ajax request to update model and send serialize data for javascript in json format

    :param request: question_id
    :return: JsonResponse
    """
    data = json.loads(request.POST["data"])
    updated_data = update_vote_data_choice_id(data)
    return JsonResponse(updated_data)


class PollsCreate(FormView):
    template_name = CREATE_POLLS_TEMPLATE
    form_class = CreatePoll
    success_url = HOME_URL

    def form_valid(self, form) -> HttpResponse:
        """
        saves the question objects received from form & get choices list and create choices objects for same question

        :param form: unknown
        :return: HttpResponse
        """
        # Save the question
        question = form.save()

        # Process choices
        choices = self.request.POST.getlist("choices")
        for choice_text in choices:
            if choice_text:
                Choice.objects.create(question=question, title=choice_text)
        return super().form_valid(form)


class PollsInfo(TemplateView):
    template_name = POLLS_INFO_TEMPLATE
