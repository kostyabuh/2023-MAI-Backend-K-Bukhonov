from django.db import models


class Worker(models.Model):
    uid = models.UUIDField(verbose_name='ID работника', primary_key=True)
    wk_first_name = models.CharField(max_length=255, verbose_name='Имя работника', blank=False)
    wk_last_name = models.CharField(max_length=256, verbose_name='Фамилия работника', blank=False)
    wk_position = models.CharField(max_length=255, verbose_name='Должность работника', blank=False)

class Client(models.Model):
    uid = models.UUIDField(verbose_name='ID клиента', primary_key=True)
    cl_first_name = models.CharField(max_length=256, verbose_name='Имя клиента', blank=False)
    cl_last_name = models.CharField(max_length=256, verbose_name='Фамилия клиента', blank=False)
    cl_number = models.CharField(max_length=256, verbose_name='Номер телефона клиента', blank=False)
    cl_passport = models.CharField(max_length=256, verbose_name='Пасспорт клиента', blank=False)



class Account(models.Model):
    uid = models.UUIDField(verbose_name='ID счета', primary_key=True)
    acc_name = models.CharField(max_length=256, verbose_name='Наименование счета', blank=False)
    acc_discr = models.CharField(max_length=256, verbose_name='Описание счета', blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Работник', blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', blank=False)
    acc_money = models.IntegerField(verbose_name='Количество денег', blank=False)

    def __str__(self):
        return f'{self.name} [{self.uid}]'

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"