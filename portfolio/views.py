from django.shortcuts import render

def index(request):
    return render(request, 'portfolioTemplates/index.html', {})

def aboutMe(request):
    return render(request, 'portfolioTemplates/aboutMe.html', {})




def projects(request):

    cards = [1,2,3,4]
    displayPannel = False


    #virker ikke edit knap
    if request.POST:
        displayPannel = True


    return render(request, 'portfolioTemplates/projects.html', {
        'cards':cards,
        'displayPannel':displayPannel,
    })