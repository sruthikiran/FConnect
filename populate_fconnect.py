import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE",fconnect.settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","fconn.settings")

import django
django.setup()

import random
from apps.fconn_app.models import College,Task,Resource

from faker import Faker

fakegen = Faker()
colleges = ['Stanford University','Santa Clara State University', 'San Jose State University','Boston College','CalTech','Georgetown','MIT']

tasks = ['fill application','ACT and/or SAT scores','Recommendation letters']

def add_college() :
    fake_city = fakegen.city()
    fake_state = fakegen.state()
    c = College.objects.get_or_create(name = random.choice(colleges),city=fake_city,state=fake_state)[0]
    c.save()
    return c

def add_task() :

    t.save()
    return t


def populate(N= 3):

    for entry in range(N):

        college = add_college()

        fake_title = random.choice(tasks)
        fake_deadline = fakegen.date()

        tsk = Task.objects.get_or_create(college=college,title=fake_title,deadline=fake_deadline)[0]

if __name__ == '__main__' :
    print("Populating Script!")
    populate(10)
    print("Populating COmplete!")
