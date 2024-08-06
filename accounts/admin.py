# -*- coding: utf-8 -*-
from accounts.models import User
from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from accounts.constants import (
    STATUS_INACTIVE_BOOL,
    STATUS_ACTIVE_BOOL,
    USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION,
    USER_ADMIN_STATUS_ACTIVE_DESCRIPTION,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_active"]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Customer Details",
            {
                "fields": [
                    "id",
                    "profile",
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password",
                    "age",
                    "address",
                    "phone",
                ]
            },
        ),
        (
            "Status Details",
            {
                "classes": ["collapse"],
                "fields": ["is_staff", "is_superuser", "is_active"],
            },
        ),
        (
            "Login Details",
            {"classes": ["collapse"], "fields": ["date_joined", "last_login"]},
        ),
        (
            "Group Details",
            {"classes": ["collapse"], "fields": ["groups", "user_permissions"]},
        ),
    ]
    search_fields = ["username"]
    list_filter = ["is_staff", "is_active", "is_superuser"]
    ordering = ["id"]
    actions = ["mark_inactive", "mark_active"]

    @admin.action(description=USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION)
    def mark_inactive(self, request, queryset):
        updated = queryset.update(is_active=STATUS_INACTIVE_BOOL)
        self.message_user(
            request,
            ngettext(
                "%d votes was successfully been reset.",
                "%d votes were successfully been reset.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description=USER_ADMIN_STATUS_ACTIVE_DESCRIPTION)
    def mark_active(self, request, queryset):
        updated = queryset.update(is_active=STATUS_ACTIVE_BOOL)
        self.message_user(
            request,
            ngettext(
                "%d votes was successfully been reset.",
                "%d votes were successfully been reset.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
