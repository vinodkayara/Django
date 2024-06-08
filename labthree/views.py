from django.shortcuts import render 
def show_lists(request):
    fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"] 
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve"] 
    context = { 
        'fruits': fruits, 'students': students 
        } 
    return render(request, 'lab3.html', context)
