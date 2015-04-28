from .models import Setting

def get(key):
    try:
        return Setting.objects.get(key = key).value
    except Setting.DoesNotExist:
        return None


def set(key, value):
    try:
        s = Setting.objects.get(key = key)
    except Setting.DoesNotExist:
        s = Setting(key = key)
    s.value = value
    s.save()

def all():
    return Setting.objects.all()