from django.shortcuts import render


def home_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        if not request.POST.get('number1') or not request.POST.get('number2'):
            context = {'resoult': 'Введите числа!!!'}
            return render(request, 'index.html', context)
        else:
            num1 = int(request.POST.get('number1'))
            num2 = int(request.POST.get('number2'))
            act = request.POST.get('action')
            if act == 'add':
                act = '+'
                resoult = num1 + num2
            elif act == 'subtract':
                act = '-'
                resoult = num1 - num2
            elif act == 'multiply':
                act = '*'
                resoult = num1 * num2
            elif act == 'divide':
                act = '/'
                if num2 == 0:
                    context = {'resoult': 'Делить на 0 нельзя'}
                    return render(request, 'index.html', context)
                else:
                    resoult = num1 / num2

            context = {
                'number1': num1,
                'number2': num2,
                'action': act,
                'resoult': resoult,
                'equals': '='
            }
            print(request.POST)
            return render(request, 'index.html', context)
