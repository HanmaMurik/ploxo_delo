from django.shortcuts import render

def index(request):
    return render(request, 'home_page.html')


def contact(request):
    return render(request, 'basic.html', {'values': ['If you have problems or you have some questions to me, message me ', '@Hanma_Murik  tg', '+9981111111111112']})

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm()


    context = {'form': form}

    return render(request, 'registration/register.html', context)
