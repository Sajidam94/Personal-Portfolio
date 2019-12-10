from django.contrib import admin

from .models import Information, Skill, Contact, Project, Education, Services


class InfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Information, InfoAdmin)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Services)
