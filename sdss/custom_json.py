from django.core.serializers.json import DjangoJSONEncoder
import datetime

class CustomJSONEncoder(DjangoJSONEncoder):
    """
    Extend Django's JSON encoder to serialize timedelta as value in seconds
    """
    def default(self, o):
        if isinstance(o, datetime.timedelta):
            return o.total_seconds()
        else:
            return super(CustomJSONEncoder, self).default(o)
