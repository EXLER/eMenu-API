from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail

from api.models import Dish


def send_new_dishes():
    emails = []
    for user in User.objects.all():
        emails.append(user.email)

    # E-mail musi zawierać informację o nowa dodanych przepisach oraz ostatnio zmodyfikowanych przepisach
    # Ale w tej aplikacji nie ma przepisów, więc założyłem że chodzi o dania
    yesterday = datetime.now().date() - timedelta(days=1)
    new_dishes = Dish.objects.filter(
        Q(created_at__gte=yesterday) | Q(updated_at__gte=yesterday)
    )

    message = "Dishes added or updated since yesterday: " + ", ".join(
        [str(dish) for dish in new_dishes]
    )

    send_mail("eMenu - new dishes", message, None, emails)