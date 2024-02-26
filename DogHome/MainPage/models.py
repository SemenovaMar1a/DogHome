from django.db import models
from django.urls import reverse
from PIL import Image
from django.core.exceptions import ValidationError


def validate_image_size_Dog(value):
    image = Image.open(value)
    width, height = image.size
    mix_width = 640
    mix_height = 640

    if width < mix_width or height < mix_height:
        raise ValidationError(f"Минимальный размеры изображения: {mix_width}x{mix_height} пикселей.")


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    GENDER_CHOICES = (
        (True, 'Мужской'),
        (False, 'Женский'),
    )
    gender = models.BooleanField(choices=GENDER_CHOICES, verbose_name='Пол')
    weight = models.IntegerField(verbose_name='Вес')
    height = models.IntegerField(verbose_name='Рост')
    description = models.TextField(blank=True, verbose_name='Описание')
    YES_NO_CHOICES = (
        (True, 'Да'),
        (False, 'Нет'),
    )
    owner = models.BooleanField(choices=YES_NO_CHOICES, verbose_name='Был ли хозяин')
    age = models.IntegerField(verbose_name='Возраст')
    color = models.CharField(max_length=100, blank=True, verbose_name='Окрас')
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, verbose_name='Название породы', blank=True, null=True,
                              default=None)
    health = models.ForeignKey('Health', on_delete=models.SET_NULL, verbose_name='Здоровье', blank=True, null=True,
                               default=None)
    shelter = models.ForeignKey('Shelter', on_delete=models.PROTECT, verbose_name='Приют', blank=True)
    photo = models.ImageField(upload_to='photos/dog/%Y/%m/%d/', verbose_name='Фото', blank=True,
                              validators=[validate_image_size_Dog])

    def get_absolute_url(self):
        return reverse('viewdog', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'


def validate_image_size_Shelter(value):
    image = Image.open(value)
    width, height = image.size
    mix_width = 550
    mix_height = 360

    if width < mix_width or height < mix_height:
        raise ValidationError(f"Минимальный размеры изображения: {mix_width}x{mix_height} пикселей.")


class Shelter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    year_of_creation = models.DateField(verbose_name='Год создания', blank=True)
    number_of_animals = models.IntegerField(verbose_name='Количество животных')
    description = models.TextField(blank=True, verbose_name='Описание')
    address = models.TextField(verbose_name='Адрес')
    contacts = models.CharField(max_length=11, verbose_name='Контакты')
    contact_person = models.CharField(max_length=100, verbose_name='Контактное лицо')
    photo = models.ImageField(upload_to='photos/shelter/%Y/%m/%d/', verbose_name='Фото', blank=True,
                              validators=[validate_image_size_Shelter])

    def get_absolute_url(self):
        return reverse('viewshelter', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приют'
        verbose_name_plural = 'Приюты'


class ShelterPhoto(models.Model):
    shelter = models.ForeignKey(Shelter, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/shelter/%Y/%m/%d/', verbose_name='Фото', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.description


def validate_image_size_Employee(value):
    image = Image.open(value)
    width, height = image.size
    mix_width = 450
    mix_height = 600

    if width < mix_width or height < mix_height:
        raise ValidationError(f"Минимальный размеры изображения: {mix_width}x{mix_height} пикселей.")


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    job_title = models.CharField(max_length=100, verbose_name='Должность')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/employee/%Y/%m/%d/', verbose_name='Фото', blank=True,
                              validators=[validate_image_size_Employee])
    shelter = models.ForeignKey(Shelter, related_name='job', on_delete=models.PROTECT, verbose_name='Место работы',
                                blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Health(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    symptoms = models.TextField(verbose_name='Симптомы', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Здоровье'
        verbose_name_plural = 'Здоровье'


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
