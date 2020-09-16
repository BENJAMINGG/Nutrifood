from django.db import models

# Create your models here.
class Produit (models.Model):
    nom des produit = models.CharField(max_lengh=80, verbose_name='Nom des produits') 
    marque = models.CharField(max_lengh=80, verbose_name='Marque')
    code = models.IntegerField()


class Ingredient (models.Model):
    ingrédient = models.ForeignKey(Produit, on_delete=models.CASCADE)
    code = models.IntegerField()
    huile de palme = models.CharField(max_lengh=80, verbose_name='Présence huile de palme')
    additif = models.CharField(max_lengh=80, verbose_name='Additif')
    trace = models.CharField(max_lengh=80, verbose_name='Trace de nutriment')

class Compte(AbstractUser):
    quota = models.IntegerField(
        blank = True,
        default = 256
    )

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    def __str__(self):
        return self.username


class Score_nutritionel (models.Model):
    nutriscore = models.CharField(max_lengh=80, verbose_name='Nutriscore')
    nutrition grade = models
    nutriment = models.ForeignKey(Produit, on_delete=models.CASCADE)
    





http://world.openfoodfacts.org/ingredients-analysis.json
GET https://[countrycode].openfoodfacts.org/api/v0/product/[barcode].json