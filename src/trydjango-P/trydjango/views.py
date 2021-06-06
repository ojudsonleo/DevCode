from django.shortcuts import render

# Create your views here.

def Graphql(request,*args, **kwargs):
    Context = {
        'key': '🔑19283',
        'urls': '/urls',
    }
    print(args, kwargs)
    return render(request, 'graphql.html', Context)


def urls(request,*args, **kwargs):
    print(args, kwargs)
    return render(request, 'graphqlurls.html')

def signlog(request,*args, **kwargs):
    print(args, kwargs)
    return render(request, 'signlog.html')