from django.shortcuts import render

# Create your views here.
posts = [{
    'customer': 'Joshua',
    'item': 'TV',
    'amount': 1000,
    'balance': 1380.90
},
    {
        'customer': 'Vincent',
        'item': 'Hoofer',
        'amount': 2500,
        'balance': 380.90
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
