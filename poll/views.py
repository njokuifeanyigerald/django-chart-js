from django.shortcuts import render, redirect
from .models import PollModel
from .forms import PollForm
from django.http import HttpResponse

def home(request):
    polls = PollModel.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    form  = PollForm(request.POST or None)
    if request.method =='POST':
        form  = PollForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['question'])
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'poll/create.html',context)


def vote(request,poll_id):
    poll = PollModel.objects.get(id=poll_id) 
    if request.method == 'POST':
        print(request.POST['poll'])
        selected = request.POST['poll']
        if selected == 'option1':
            poll.optionOneCount += 1
        elif selected == 'option2':
            poll.optionTwoCount += 1
        elif selected == 'option3':
            poll.optionThreeCount += 1
        else:
            return HttpResponse(400, 'invalid form')
        poll.save()
        return redirect('results', poll.id)
    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)



def results(request,poll_id):
    poll = PollModel.objects.get(id=poll_id)
    context = {'poll': poll}
    return render(request, 'poll/results.html', context)



