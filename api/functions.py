from pathlib import Path


def get_image_path(instance, filename):
    return Path("media", filename)