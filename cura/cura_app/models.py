from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    # @property
    # def beds(self):
    #     return Bed.objects.filter(name__contains=')


class Bed(models.Model):
    bed_number = models.CharField(max_length=200)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.bed_number


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AllocationRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    allocation_start_date = models.DateField('Start datum')
    allocation_end_date = models.DateField('Eind datum', blank=True, null=True,)
    preferred_locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.client.name


class BedClientAllocations(models.Model):
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    allocation_start_date = models.DateField('Start datum')
    allocation_end_date = models.DateField('Eind datum', blank=True, null=True,)

    def __str__(self):
        return self.bed.bed_number
