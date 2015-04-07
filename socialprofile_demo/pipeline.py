from django.shortcuts import redirect

from social.pipeline.partial import partial

import subprocess 


def syncipa(backend, details, response, uid, user, *args, **kwargs):
  username = self.kwargs.get('username')
  subprocess.Popen(["/root/user_management.sh", username])
