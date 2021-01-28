from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    
    messager = models.TextField('Текст сообщения', error_messages={'required': 'это поле обязательно'})
    
    mess = models.ForeignKey(User, on_delete=models.CASCADE)
    
    ball=models.SmallIntegerField('Количество баллов')
    
    
    def __str__(self):
        
        return self.messager
    
    
    class Meta:
        
        verbose_name = 'список достижений'
        
        verbose_name_plural = 'список достижений'
       
        ordering = ['id']

