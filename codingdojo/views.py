from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from codingdojo.models import Lender, Borrower, Loan
from django.core.exceptions import ValidationError
from django.contrib import messages
from datetime import datetime

# Create your views here.

def index(request):
	print (request.GET)
	print (request.method)
	return render(request, 'cores/index.html')

def register(request):
    return render(request, 'cores/register.html', {})

def lender_register(request):
	print ("Registration for Lender")
	lender = Lender.objects.filter(email = request.POST.get('email'), password=request.POST.get('password'))
	if len(lender) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		lender = Lender()
		lender.first_name = request.POST.get('fnamel')
		lender.last_name = request.POST.get('lnamel')
		lender.email = request.POST.get('email')
		lender.password = request.POST.get('password')
		lender.money = request.POST.get('money')
		lender.created_at = datetime.now()
		lender.updated_at = datetime.now()
		lender.save()
		print ("Successful Registration")
		print (lender.email)
		print (lender.password)
		return redirect('/')

def borrower_login_page(request):
	return render(request, 'cores/borrower_login.html')


def lender_login_page(request):
	return render(request, 'cores/lender_login.html')

	
def borrower_register(request):
	print ("Borrower register")
	borrower = Borrower.objects.filter(
		email = request.POST.get('email')
		)
	if len(borrower) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		borrower = Borrower()
		borrower.first_name = request.POST.get('fnameb')
		borrower.last_name = request.POST.get('lnameb')
		borrower.email = request.POST.get('email')
		borrower.password = request.POST.get('password')
		borrower.needed = request.POST.get('needed')
		borrower.purpose = request.POST.get('purpose')
		borrower.description = request.POST.get('description')
		borrower.raised = 0
		borrower.amount = 0
		borrower.created_at = datetime.now()
		borrower.updated_at = datetime.now()
		borrower.save()
		print ("Successful Registration")
		print (borrower.email)
		print (borrower.password)
		print (borrower.purpose)
		print (borrower.description)
		print (borrower.raised)
		print (borrower.needed)
		return redirect('/')


def borrower_login(request):
	print ("Borrower Login")
	print (request.POST.get('email'))
	print (request.POST.get('password'))
	borrower = Borrower.objects.filter(email = request.POST.get('email'))
	if len(borrower) <1:
		print ("Failed")
		return redirect('/')
	else:
		print ("Success")
		request.session['borrower_id'] = borrower[0].id
		print ("Logged in")
		return redirect('/borrower_home')


def borrower_home(request):
		print ("Borrower Home")
		if "borrower_id" in request.session:
			lender = Lender.objects.all()
			borrower = Borrower.objects.get(id=request.session['borrower_id'])
			loans = borrower.loan_set.all()
			content = {
			'lender': lender,
			'borrower': borrower,
			'loans': loans,
		}
			return render(request, 'cores/borrower_home.html', content)
		else:
			del request.session
			return redirect('/')


def lender_login(request):
	print ("Lender Login")
	print (request.POST.get('email'))
	lender = Lender.objects.filter(email = request.POST.get('email'), password = request.POST.get('password'))
	if len(lender) <1:
		print ("Failed")
		return redirect('/')
	else:
		print ("Success")
		request.session['lender_id'] = lender[0].id
		return redirect('/lender_home')



def lender_home(request):
	print ("Lender Home")
	if "lender_id" in request.session:
		lender = Lender.objects.get(id=request.session['lender_id'])
		loans = lender.loan_set.all()
		borrowers = Borrower.objects.exclude(loan__in = lender.loan_set.all())
		content = {
			'lender': lender,
			'borrowers': borrowers,
			'loans': loans,
		}
		return render(request, 'cores/lender_home.html', content)
	else:
		del request.session
		return redirect('/')



def lend(request, borrower_id):
	if request.method == 'POST':
		print ("In Lending")
		lender = Lender.objects.get(id=request.session['lender_id'])
		borrower = Borrower.objects.get(id=borrower_id)
		lender.money -= float(request.POST.get('amount'))
		if lender.money < 0:
			return HttpResponse('Insufficent funds')
		elif lender.money < float(request.POST.get('amount')):
			return HttpResponse('Cannot process. There are no funds left')
		else:
			lender.save()
			borrower.raised += float(request.POST.get('amount'))
			borrower.needed -= float(request.POST.get('amount'))
			borrower.save()
			loan = Loan.objects.create(lender=lender, borrower=borrower, amount=float(request.POST.get('amount')))
			return redirect ('/lender_home')

def delete(request, borrower_id):
	print ("Unfunding")
	borrower = Borrower.objects.get(id=borrower_id)
	lender = Lender.objects.get(id=request.session['lender_id'])
	lender.money += 25
	lender.save()
	loan = Loan.objects.get(lender=lender, borrower=borrower, amount=25)
	loan.amount = 0
	loan.save()
	borrower.needed +=25
	borrower.raised -=25
	borrower.save()
	print (loan)
	return redirect('/lender_home')



def lender_logout(request):
	print ("Logging out")
	del request.session['lender_id']
	return redirect('/')



def borrower_logout(request):
	print ("Logging out")
	del request.session['borrower_id']
	return redirect('/')