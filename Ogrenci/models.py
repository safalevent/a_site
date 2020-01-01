from django.db import models

class Ogrenci(models.Model):
    İsim = models.CharField(max_length=100)
    Soyisim = models.CharField(max_length=100)
    E_mail = models.EmailField(max_length=100)
    Doğum_Tarihi = models.DateField()
    Okulu = models.CharField(max_length=100)
    Bölümü = models.CharField(max_length=100)
    Siniflar = (("h","Hazırlık"),("1","1"),("2","2"),("3","3"),("4","4"))
    Sınıfı = models.CharField(max_length=1, choices = Siniflar,default="1")

    def sinif_atla(self):
        self.Sinifi = Siniflar[Siniflar.index(self.Sinifi)+1]

    def __str__(self):
        return self.İsim + " " + self.Soyisim
