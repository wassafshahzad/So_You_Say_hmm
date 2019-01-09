from channels.routing import ProtocolTypeRouter
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
