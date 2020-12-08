from django.db import models

# Create your models here.

class Lender(models.Model):
	first_name = models.TextField(blank=False, max_length=20)
	last_name = models.TextField(blank=False, max_length=20)
	email = models.TextField(blank=False, max_length=20)
	password = models.TextField(blank=False)
	money = models.IntegerField(blank=False)
	total_left = models.IntegerField(blank=False, null=True)

class Borrower(models.Model):
	first_name = models.TextField(blank=False, max_length=20)
	last_name = models.TextField(blank=False, max_length=20)
	email = models.TextField(blank=False, max_length=20)
	password = models.TextField(blank=False, max_length=20)
	amount = models.IntegerField(blank=False)
	purpose = models.TextField(blank=False, max_length=50)
	description = models.TextField(blank=False, max_length=100)
	raised = models.IntegerField(blank=False)
	needed = models.IntegerField(blank=False, null=True)
	total_left = models.IntegerField(blank=False, null=True)
	created_at = models.DateField()
	updated_at = models.DateField()

class Loan (models.Model):
    amount = models.IntegerField(null=True)
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)