def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join([items[0], items[1]])
    elif len(items) > 2:
        last_item = ', and '.join([items[-2], items[-1]])
        items.pop()
        items.pop()
        items.append(last_item)
        return ', '.join(items)
