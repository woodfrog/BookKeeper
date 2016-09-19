from django.db import models


class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return 'Group No.{}'.format(self.group_id)


class Person(models.Model):
    groups = models.ManyToManyField(Group)
    person_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return 'Person id{}'.format(self.person_id)


class Bill(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    payer = models.ForeignKey(Person, related_name='payer')
    consumers = models.ManyToManyField(Person, related_name='consumers')
    bill_id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    bill_description = models.TextField(max_length=200)

    def __str__(self):
        return 'Bill No.{} with price {}'.format(self.bill_id, self.price)
