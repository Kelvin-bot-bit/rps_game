from django.shortcuts import render
import random

choices = ['rock', 'paper', 'scissors']


def play(request):
    result = None
    user_choice = None
    computer_choice = None

    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = 'Draw'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            result = 'You Win 🎉'
        else:
            result = 'You Lose 😢'

    return render(request, 'game/play.html', {
        'result': result,
        'user_choice': user_choice,
        'computer_choice': computer_choice
    })
