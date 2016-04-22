def get(key):
    from .models import Setting
    import json
    # key can be "alerting.ficon.*" or without asterisk
    # value can be a plain string or a json object

    if len(key) == 0:
        raise Exception("An empty key was received")

    if key[-1] == "*":
        d = {}
        for s in Setting.objects.filter(key__startswith = key[:-1]):
            d.update({s.key: json.loads(s.value)})
        return d

    # let it raise an exception if the key is not found
    return json.loads(Setting.objects.get(key = key).value)

def set(key, value):
    from .models import Setting
    import json
    try:
        s = Setting.objects.get(key = key)
    except Setting.DoesNotExist:
        s = Setting(key = key)
    s.value = json.dumps(value)
    s.save()

def all():
    from .models import Setting
    import json
    d = {}
    for s in Setting.objects.all():
        d.update({s.key: json.loads(s.value)})
    return d
