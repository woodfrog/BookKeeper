from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=20, unique=True)
    total_expense = models.IntegerField(default=0)

    def __str__(self):
        return 'Group {}'.format(self.group_name)

    class Meta:
        ordering = ('group_name',)

    def add_a_person(self, person):
        self.person_set.add(person)
        person.groups.add(self)
        new_record = Record(group=self, person=person, amount=0)
        new_record.save()
        self.record_set.add(new_record)
        self.save()

    # add a new bill record into the group
    def record_a_bill(self, bill):
        self.bill_set.add(bill)
        self.total_expense += bill.price
        self.save()


class Person(models.Model):
    groups = models.ManyToManyField(Group) # one person can be in many groups at a time
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return 'Person name:{}'.format(self.name)

    class Meta:
        ordering = ('name',)


class Bill(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    payer = models.ForeignKey(Person, related_name='payer')
    consumers = models.ManyToManyField(Person, related_name='consumers')
    price = models.IntegerField()
    bill_description = models.TextField(max_length=200)

    def __str__(self):
        return 'Bill with price {}'.format(self.price)


class Record(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
