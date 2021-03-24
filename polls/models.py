from django.db import models

# Create your models here.
class Org(models.Model):
    org_name = models.CharField(("Имя организаций"), max_length=50,null=True)
    f_name = models.CharField(("ФИО"), max_length=50,null=True)
    position = models.CharField(("Должность"), max_length=50,null=True)

    def __str__(self):
        return self.f_name

class Staff(models.Model):
    f_name = models.CharField(("ФИО исполнителя"), max_length=50,null=True)
    position = models.CharField(("Должность"), max_length=50,null=True)
    phone_number = models.CharField(("Телефон"),max_length=12,null=True)

    def __str__(self):
        return self.f_name


class Mail(models.Model):
    nomer = models.AutoField(("Исходяший номер"),primary_key=True)
    date_mail = models.DateField("Дата",null=True)
    sent_to = models.ForeignKey(Org,on_delete=models.CASCADE,null=True)
   # sent_to = models.CharField(("Кому"), max_length=50)
    sender = models.CharField(("От кого"), max_length=50,null=True)
    mail = models.TextField(("Писмо"),null=True)
    executor = models.ForeignKey(Staff, on_delete=models.CASCADE,null=True)
    #executor = models.CharField(("Исполнитель"), max_length=50)

    def __str__(self):
        return self.sender

    class Meta:
       ordering = ['date_mail'] 
