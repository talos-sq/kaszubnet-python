from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.urls import reverse

RANKS = [
    (0, 'Kapitan'),
    (1, 'Sztabowy'),
    (2, 'Przystaniowiec'),
    (3, 'Rekrut'),
]

FUNCTION = [
    (0, 'brak'),
    (1, 'Kwatermistrz'),
]

OUTPOSTS = [
    (0, 'O.R.P Kaszub'),
    (1, 'OldTown'),
    (2, 'TriCity'),
    (3, 'Północ'),
    (4, 'Nomad'),
]

ITEM_TYPE = [
    (0, 'Nieznany'),
    (1, 'Użytkowy'),
    (2, 'Materiał do produkcji'),
    (3, 'Medyczny'),
    (4, 'Elektronika'),
]

ACTION_TYPE = [
    (0, 'Dodanie'),
    (1, 'Wybranie'),
]


class OTs(models.Model):
    year = models.IntegerField(null=True, validators=[MinValueValidator(2103)], verbose_name="Pory przybyszów")

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Edycja OT"
        verbose_name_plural = "Edycje OT"


class Ability(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa umiejętności")
    level = models.IntegerField(blank=True, null=True, verbose_name="Poziom")
    description = models.TextField(blank=True, verbose_name="Opis")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Umiejętność"
        verbose_name_plural = "Umiejętności"


class Character(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa postaci")
    owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE, verbose_name="Właściciel")
    birthdate = models.DateField(null=True, blank=True)
    rank = models.IntegerField(choices=RANKS, default=2, verbose_name="Ranga")
    function = models.IntegerField(choices=FUNCTION, default=0, verbose_name="Funkcja")
    abilities = models.ManyToManyField(Ability, blank=True, verbose_name="Umiejętności")
    outpost = models.IntegerField(choices=OUTPOSTS, default=4, verbose_name="Placówka")
    origin_outpost = models.CharField(blank=True, max_length=64, verbose_name="Miejsce pochodzenia")
    job = models.CharField(blank=True, max_length=64, verbose_name="Zawód")
    specialization = models.CharField(blank=True, max_length=64, verbose_name="Specjalizacje")
    religion = models.CharField(blank=True, max_length=64, verbose_name="Wiara")
    character_history = models.TextField(null=True, blank=True)
    old_town_presence = models.ManyToManyField(OTs, null=True, blank=True, verbose_name="Pory Przybyszów")
    dead = models.BooleanField(null=True, blank=True, verbose_name="Czy postać zmarła?")
    left_faction = models.BooleanField(null=True, blank=True, verbose_name="Czy postać opuściła frakcje?")
    picture = models.BinaryField(null=True, blank=True, verbose_name="Zdjęcie")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Postać"
        verbose_name_plural = "Postaci"


class WarehouseItems(models.Model):
    item_name = models.CharField(max_length=64, verbose_name="Nazwa przedmiotu")
    item_type = models.IntegerField(choices=ITEM_TYPE, verbose_name="Typ przedmiotu")
    item_amount = models.IntegerField(null=True, blank=True, verbose_name="Ilosć")
    item_description = models.TextField(null=True, blank=True, verbose_name="Opis przedmiotu")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('warehouse-status')

    class Meta:
        verbose_name = "Przedmiot zmagazynowany"
        verbose_name_plural = "Przedmioty zmagazynowane"


class WarehouseLog(models.Model):
    item = models.ForeignKey(WarehouseItems, on_delete=models.PROTECT, null=True, verbose_name="Przedmiot")
    action = models.IntegerField(choices=ACTION_TYPE, verbose_name="Akcja")
    amount = models.IntegerField(null=True, verbose_name="Ilość")
    issuer = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE, verbose_name="Właściciel")
    log_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = "Ewidencja magazynowa"
        verbose_name_plural = "Ewidencja magazynowa"


class Artefact(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa artefaktu")
    description = models.TextField(verbose_name="Opis artefaktu")

    class Meta:
        verbose_name = "Artefakt"
        verbose_name_plural = "Artefakty"
