from django.shortcuts import redirect

from social.pipeline.partial import partial

import subprocess 


def syncipa(backend, details, response, uid, user, *args, **kwargs):
    print('=' * 80)
    print('response')
    print('=' * 80)
    pprint(response)
    print('=' * 80)
    print('details')
    print('=' * 80)
    pprint(details)
    print('=' * 80)
    print('args')
    print('=' * 80)
    pprint(args)
    print('=' * 80)
    print('kwargs')
    print('=' * 80)
    pprint(kwargs)
    print('=' * 80)
    subprocess.Popen(["/root/user_management.sh", "username", "first-name", "last-name", "email"])
