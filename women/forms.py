# from django import forms
# # from django.core.exceptions import ValidationError
# from women.models import Women
# # from .models import *
        #
        # fields = ['first_name',
        #           'last_name',


from django import forms
from women.models import Women


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Категория не выбрана"
        self.fields["is_published"].initial = True


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = "__all__"

# '__all__'
#
# class AddPostForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100, label="Имя", required=False)
#     last_name = forms.CharField(max_length=100, label="Фамилия")
#     age = forms.IntegerField(label="Возраст")
#     bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Биография")
#     is_published = forms.BooleanField(label="Опубликован", required=False, initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")



