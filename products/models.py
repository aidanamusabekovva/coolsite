from django.db import models
#
class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=1)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

# классы CharField - str,
# 255 - 1 bite
# null=True в базе данных для данного поля одно значение нал, проверка на уровне базы данных,
# бланк =тру проверка формы,позволит оставить поле пустым при отправке формы


#
def __str__(self):
    return self.title


class AnimalCategory(models.Model):
    name = models.CharField(max_length=100)


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    breed = models.CharField(max_length=100)
    # breed_category = models.ForeignKey(
    #     AnimalCategory,
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    

    def __str__(self):
        return self.name