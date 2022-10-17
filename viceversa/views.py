from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    text_words= user_text.split()
    count_words=len(text_words)
    user_text_reverse = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'countwords': count_words, 'usertextreverse': user_text_reverse})
