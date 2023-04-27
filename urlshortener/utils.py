from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)
AVAILABLE_CHARS = ascii_letters + digits


def create_random_url(chars=AVAILABLE_CHARS):
    # Creates a random string with the predetermined size

    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    random_url = create_random_url()
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_url).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_url
