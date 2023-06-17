from django.db import models
import random
from string import ascii_letters,digits
from django.utils import timezone
# Create your models here.

#storing all character whic are allowed in base62
BASE62CHARACTERS = ascii_letters+digits

class ShortLink(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True,blank=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True,blank=True)
    
    class Meta:
        ordering=["-created"] #order based on newly created link
        
    def __str__(self) -> str:
        return f"{self.long_url} to {self.short_url}" #it will show like this 
    
    
    #modifying built in save funciton 
    
    def save(self, *args,**kwargs):
        #if short_url is empty , not generated yet
        if not self.short_url:
            self.short_url = self.generate_short_url() #calling funciton to generate short url
              
        if self.last_accessed and (timezone.now()-self.last_accessed).days>=365:
            self.short_url=""   
        #update the last accessed time 
        self.last_accessed = timezone.now()
        super().save(*args, **kwargs)
        
        
    def generate_short_url(self):
        #loop will be iterate until find unique code
        while True:
            short_code = "".join(random.choices(BASE62CHARACTERS,k=7)) #generating short code
            if not ShortLink.objects.filter(short_url=short_code).exists(): #checking from data base that shor_code is exist or not
                return short_code #if not exist in database then return
    
    
    