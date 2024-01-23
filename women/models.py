from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Women(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    age = models.IntegerField(default=18)
    nationality = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="women/", null=True, blank=True)
    catefory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# class Meta:
#     verbose_name = "женщины"
#     verbose_name_plural = "Известные женщины"
#     ordering = ["-time_create", "title"]
    # один к одному
    # один кo многим
    # много к многому
    # set_null
    # cascade
    # protect

# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Women
#         fields = ['first_name', 'last_name', 'age', 'nationality', 'bio', 'category']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-input'}),
#             'bio': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
#         }
#
#     def clean_title(self):
#         first_name = self.cleaned_data['first_name']
#         if len(first_name) > 50:
#             raise ValidationError('имя больше 50 символов')
#
#         return first_name

#


