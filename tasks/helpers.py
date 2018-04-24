from .models import Category


def get_categories(lang='en'):
    categories = Category.objects.filter(is_active=True)
    categories_list = []
    for category in categories:
        temp = (category.id, category.title)
        categories_list.append(temp)
    return categories_list