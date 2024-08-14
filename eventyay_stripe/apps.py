from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Python package 'stripe' is not installed.")


class StripePluginApp(AppConfig):
    default = True
    name = 'eventyay_stripe'
    verbose_name = _("Stripe")

    class PretixPluginMeta:
        name = _("Stripe")
        author = "eventyay"
        version = __version__
        category = 'PAYMENT'
        featured = True
        visible = True
        description = _("This plugin allows you to receive credit card payments " +
                        "via Stripe.")

    def ready(self):
        from . import signals, tasks  # NOQA


default_app_config = 'eventyay-stripe.apps.StripePluginApp'
