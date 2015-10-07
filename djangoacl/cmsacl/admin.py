from django.contrib import admin
from django.forms import ModelChoiceField
from .models import CMSAction



# class Invoice(models.Model):
#       person = models.ForeignKey(Person)
#       ....
#
# class InvoiceAdmin(admin.ModelAdmin):
#       form = MyInvoiceAdminForm



# class CustomModelChoiceField(ModelChoiceField):
#      def label_from_instance(self, obj):
#          return "%s %s" % (obj.first_name, obj.last_name)
#
#
# class MyInvoiceAdminForm(forms.ModelForm):
#     person = CustomModelChoiceField(queryset=Person.objects.all())
#
#     class Meta:
#           model = Invoice





class ActionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('users', 'groups')

admin.site.register(CMSAction, ActionAdmin)
