#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from ast import IsNot
from contextlib import nullcontext
import os
import sys
from stockproject import views

def main():
    if len(sys.argv[1])> 5 and sys.argv[2]:
        stock = sys.argv[2]
        firstValue = sys.argv[3]
        secondValue = sys.argv[4]
        server = True
    elif len(sys.argv[4]) > 5 and sys.argv[2]:
        stock = sys.argv[1]
        firstValue = sys.argv[2]
        secondValue = sys.argv[3]
        server = True
    elif sys.argv[2]:
        stock = sys.argv[1]
        firstValue = sys.argv[2]
        secondValue = sys.argv[3]
        server = False
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if stock is None or firstValue is None or secondValue is None:
        raise Exception(
            "                                                            "
            "                                                            "
            "Sorry, you must insert a Stock symbol like 'PETR4' "
            "and valid values for stock monitoring, such as: 20.9 30.6 "
            "Why don't you give it a try again?"
            "execute 'python manage.py petr4 19.5 27.9' "
            "or 'python manage.py petr4 27.9 19.5 runserver' to test each function by route"
        )

    views.Test(stock, firstValue, secondValue)
    if server:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
