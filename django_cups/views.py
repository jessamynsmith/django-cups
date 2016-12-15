import json as simplejson

from django.shortcuts import render, get_object_or_404
from django_cups.models import Printer, FavouritePrinter
from django.http import HttpResponse


def displayPrintForm(request):
    return render(request, 'django_cups/print_form.html', {})


def getPrinterslist(request):
    '''
    return the printers list
    '''
    printers = Printer.objects.all()
    return render(request, 'django_cups/printers_list.html', {'printers': printers})


def getFavouriteslist(request):
    '''
    return favourite printers list
    '''
    printers = []
    if request.user.is_authenticated():
        printers = FavouritePrinter.objects.getFavourites(request.user)
    return render(request, 'django_cups/favourites_list.html', {'printers': printers})


def addFavourite(request, printer_id):
    '''
    add a new printer to favourites
    '''
    printer = get_object_or_404(Printer, pk=printer_id)
    status = False
    if request.user.is_authenticated():
        printer.addToFavourite(request.user)
        status = True
    return HttpResponse(simplejson.dumps({'status': status}))


def delFavourite(request, printer_id):
    '''
    remove a favourite printer
    '''
    printer = get_object_or_404(Printer, pk=printer_id)
    status = False
    if request.user.is_authenticated():
        printer.delFromFavourite(request.user)
        status = True
    return HttpResponse(simplejson.dumps({'status': status}))


def refreshPrinterslist(request):
    '''
    refresh printers cache list
    '''
    Printer.objects.updatePrinters()
    return HttpResponse(simplejson.dumps({'status': True}))
