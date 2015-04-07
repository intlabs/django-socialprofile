from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse


def send_validation(strategy, backend, code):
    url = '{0}?verification_code={1}'.format(
        reverse('social:complete', args=(backend.name,)),
        code.code
    )
    url = strategy.request.build_absolute_uri(url)

    subject, from_email, to = 'CannyOS - Validate your account', settings.EMAIL_FROM, code.email
    text_content = 'This is an important message from CannyOS; in order to continue you will need to validate your account {0}'.format(url)
    html_content = '<p>This is an <strong>important</strong> message from CannyOS; in order to continue you will need to validate your account {0}</p>'.format(url)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
