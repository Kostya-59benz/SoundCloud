
from django.core.exceptions import ValidationError

def get_path_upload_avatar(instance, file):
    """ Построение пути к файлу, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def validate_size_image(file_obj):

    megabite_limit = 2
    if file_obj.size > megabite_limit * 1024 * 1024:
        raise ValidationError(f" Max size of file is {megabite_limit}MB")