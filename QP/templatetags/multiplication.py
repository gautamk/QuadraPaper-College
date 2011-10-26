#!/usr/bin/python
#
#
#
#
#
#
#
#
#
from django import template
register = template.Library()
@register.filter
def multiplication(multiplicand , multiplier):
    try:
        return ( int(multiplicand) * int(multiplier) )
    except ValueError:
        return ""




if __name__ == "__main__":
    pass
    
