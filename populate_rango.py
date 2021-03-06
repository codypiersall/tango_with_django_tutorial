import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat,
             title='Official Python Tutorial',
             url='http://docs.python.org/3/tutorial')

    add_page(cat=python_cat,
             title="How to think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat('Django', views=64, likes=32)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
             title="How to =Tango with Django",
             url='http://www.tangowithdjango.com/')

    frame_cat = add_cat('Other Frameworks', views=32, likes=16)

    add_page(frame_cat,
             title='Bottle',
             url='http://bottlepy.org/docs/dev/')

    add_page(frame_cat,
             title='Flask',
             url='http://flask.pocoo.org')

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {} - {}'".format(str(c), str(p)))


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


if __name__ == '__main__':
    print('Starting Rango population script...')
    import sys
    if len(sys.argv)> 1 and sys.argv[1] == 'delete':
        print('deleting all objects')
        Category.objects.all().delete()
        Page.objects.all().delete()
    else:
        populate()
