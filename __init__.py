from .models import Setting

def get(key):
    # key could be "alarming.ficon.*"
    
    if len(key) == 0:
        raise Exception("An empty key was received")
    
    if key[-1] == "*":
        return { s.key: s.value for s in Setting.objects.filter(key__startswith = key[:-1]) }
    
    # let it raise an exception if the key is not found
    return Setting.objects.get(key = key).value

def set(key, value):
    try:
        s = Setting.objects.get(key = key)
    except Setting.DoesNotExist:
        s = Setting(key = key)
    s.value = value
    s.save()

def all():
    return { s.key: s.value for s in Setting.objects.all() }