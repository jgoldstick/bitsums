from django.shortcuts import render

import datetime
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import BitSum
from .forms import BitSumForm


def bitsum(request):
    count = BitSum.objects.count()
    bitsum = 0
    A = request.GET.get('A', None)
    if A is None:
        return HttpResponseBadRequest("No value for A")
    B = request.GET.get('B', None)
    if B is None:
        return HttpResponseBadRequest("No value for B")
    try:
        A = int(A)
        B = int(B)
    except ValueError:
        return HttpResponseBadRequest("A and B must be integers")

    binary = bin(A*B)[2:]
    for b in binary:
        if b == '1':
            bitsum += 1

    bit_sum = BitSum()
    bit_sum.A = A
    bit_sum.B = B
    bit_sum.bitsum = bitsum
    bit_sum.time = datetime.datetime.now()
    bit_sum.used = count + 1
    bit_sum.save()

    now = bit_sum.time
    return JsonResponse({'time': now, 'bitsum': bitsum, 'A': A, 'B': B, 'used': count})


def history_form(request):
    """
    lists the previous bitsums and provides a form to enter a new query
    """
    bitsums = BitSum.objects.all()
    if request.method == 'POST':
        form = BitSumForm(request.POST)
        if form.is_valid():
            A = form.cleaned_data['A']
            B = form.cleaned_data['B']
            url = "bitsum?A=%d&B=%d" % (A, B)
            return HttpResponseRedirect(url)
    else:
        form = BitSumForm()
        return render(request, "bitsum/templates/entry_form.html", {'form': form, 'bitsums': bitsums})


def instructions(request):
    """
    Instructions for this exercise
    """
    return render(request, 'bitsum/templates/instructions.html')
