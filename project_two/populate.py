import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')

import django
django.setup()

import random
from app_two.models import AccessRecord, Topic, WebPage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fakeurl = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top, url=fakeurl, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating Database.')
    populate(12)
    print('Done.')
