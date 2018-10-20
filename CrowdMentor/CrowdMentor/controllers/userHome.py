from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from CrowdMentor.models import Profile

dict_roles= {'UserRoles.WORKER': 'worker', 'UserRoles.TASK_UPDATER': 'task_updater', 'UserRoles.AUDITOR': 'auditor',
             'UserRoles.ADMIN': 'admin', 'UserRoles.MENTOR': 'mentor'}


@login_required
def view(request):
    user_id = User.objects.get(username=request.user.username).id
    profile = dict_roles[Profile.objects.get(user_id=user_id).role]
    dict_functs={'/tasks/': 'View open tasks', '/tasks/claimed': 'View claimed tasks'}
    if profile == 'task_updater' or profile == 'admin':
        dict_functs['/tasks/add_tasks']= 'Add task'

    return render(request, 'home.html', {"profile": profile, "dict_functs" : dict_functs})