from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    img=models.ImageField(default='default.jpg', upload_to='profiles')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        imge=Image.open(self.img.path)
        if imge.height>300 or imge.width>300:
            size=(300,300)
            imge.thumbnail(size)
            imge.save(self.img.path)