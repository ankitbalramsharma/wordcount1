from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    list_length=len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            # increase value by 1
            worddictionary[word] += 1
        else:
            # add to the worddictionary and set value to 1
            worddictionary[word] = 1

    sorted_List = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True) # by default it is in ascending order. In oreder to make it descending order

    return render(request,'count.html', {'fulltext':data, 'words':list_length, 'worddictionary':sorted_List})

def about(request):
    return render(request,'about.html')
