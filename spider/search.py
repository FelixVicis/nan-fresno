import googlesearch as google


def websites(query, start=0, stop=None, per_page=10):
    return google.search(query, start=start, stop=stop, num=per_page)


def images(query, start=0, stop=None, per_page=10):
    return google.search_images(query, start=start, stop=stop, num=per_page)
