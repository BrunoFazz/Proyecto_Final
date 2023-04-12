from perfil.models import Avatar


def clean_avatar_record_without_user():
    Avatar.objects.filter(user_id=None).delete()
