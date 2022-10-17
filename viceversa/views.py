from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    user_text_reverse = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'usertextreverse': user_text_reverse})
