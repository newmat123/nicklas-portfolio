from django.shortcuts import render
from .models import imgs
from .forms import ImgForm


def index(request):
    return render(request, 'portfolioTemplates/index.html', {})

def aboutMe(request):
    return render(request, 'portfolioTemplates/aboutMe.html', {})


def projects(request):

    cards = [1,2,3,4]
    imgform = ImgForm()
    displayPannel = False
    edit = False
    langimgs = None

    if request.method == 'POST':

        if request.POST.get('addNewProject'):
            displayPannel = True
        
        #uploads a new imge to the db
        if request.POST.get('uploadimg'):
            form = ImgForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        
        if request.POST.get('deleteimg'):
            img_id = request.POST.get('deleteimg')
            print(img_id)
            form = ImgForm(instance=imgs.objects.get(id=img_id),data=request.POST)

            if form.is_valid():
                theimage = form.save(commit=False)
                theimage.delete()



        #edit a element
        if request.POST.get('editCard'):
            langimgs = imgs.objects.all()
            displayPannel = True
            edit = True

    return render(request, 'portfolioTemplates/projects.html', {
        'cards':cards,
        'displayPannel':displayPannel,
        'edit':edit,
        'imgform':imgform,
        'langimgs':langimgs,
    })