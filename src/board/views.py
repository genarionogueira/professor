from django.shortcuts import render
from django.shortcuts import redirect

def mainBoardView(request):
    
    if not request.user.is_authenticated:
        return redirect('/login')
    
    return render(request, 'board/mainBoard.html')


