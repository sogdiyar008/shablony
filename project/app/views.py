from django.shortcuts import render

def index(request):
    data={'study':'Alabuga Polytech',
          'group':'315-8, Python-1',
          'speciality':'Младший Специалист',
          'after':'Разработчиком'}
    return render(request, 'app/index.html', context=data)

def about(request):
    data={'FIO':'Бахтияров Согдияр Бахтияярович',
          'height':'185см',
          'weight':'80кг',
          'age':'16'}
    return render(request, 'app/about.html', context=data)

def contacts(request):
    data={'dates':{'number':'+7 950 321 98 69',
                   'insta':'Sogdiyar008',
                   'Telegramm':'@sogdiyar007',
                   'numder1':'+996 706 79 11 25'}}
    return render(request,'app/contacts.html', context=data)


def form (request):
    return render(request, 'app/form.html')