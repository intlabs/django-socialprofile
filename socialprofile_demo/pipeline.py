from django.shortcuts import redirect

from social.pipeline.partial import partial

import subprocess 


def syncipa(backend, details, response, uid, user, *args, **kwargs):
  subprocess.Popen(["/usr/bin/touch", "/root/bingo"])
