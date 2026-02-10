from django import template
from rango.models import Category

from typing import TypedDict, Any, Optional

class CategoryListContext(TypedDict):
    categories: Any
    current_category: Optional[Category]

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category: Optional[Category]=None) -> CategoryListContext:
    return {'categories': Category.objects.all(),
            'current_category': current_category}
