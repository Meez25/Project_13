from django.shortcuts import render
from lettings.models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# luctus et ultrices posuere cubilia curae; Cras eget scelerisque

def index(request):
    """
    View function to render the index page.

    Retrieves a list of all available lettings and passes it to the template
    for rendering.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat
# pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas
# auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit
# libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque
# justo mattis ullamcorper ac non tellus. In tristique mauris eu velit
# fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor
# elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac
# lacinia augue pulvinar sit amet.

def letting(request, letting_id):
    """
    View function to render details for a specific letting.

    Retrieves a letting object based on the provided letting_id and passes
    it to the template for rendering.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
