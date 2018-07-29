import spider as s
import identifier as i

known_images = [
    # {
    #     'url': 'Image of the person you are searching for.',
    #     'name': 'Name to report on find',
    #     'query': 'Selected terms to help find the person',
    # },
]

known_false = [
]


config = {
    'found': False,
    'limit': 300,
    'known_images': known_images
}


def scrape(query, limit=1000, found=False, **kwargs):
    count = 0

    print('Searching for "{query}"\nWill exit when:\n\tSearched {limit} images\n\t{is_found}'
          .format(query=query,
                  limit=limit,
                  is_found='Person is found' if found else 'Search Terminates'))

    for image in s.get_image_urls(query):
        if not image:
            continue

        count += 1

        print('Scanning ({count}/{limit}): {url}\n'.format(
            count=count,
            limit=limit,
            url=image))

        is_found = i.test_for_known_faces(image)

        if is_found:
            for face in is_found:
                if image in known_false:
                    print('False match: {name} at {image}'.format(name=face['name'], image=image))
                else:
                    # face['image']['image'].show()
                    print('Found {name}({source_url})\nat {url}\n\n'.format(
                        name=face['name'],
                        source_url=face['for']['url'],
                        url=image
                    ))

        if is_found and found:
            print('Exiting because found.')
            return

        if count >= limit:
            print('Exiting exceeded limit')
            return

    print('Exiting search terminated')


def runner(known_images, **config):
    for image in known_images:
        i.add_known_image(**image)

    for image in known_images:
        scrape(**image, **config)


runner(**config)
