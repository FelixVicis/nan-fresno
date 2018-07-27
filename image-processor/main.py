#!/usr/bin/python3
import face_recognition
import open_image

known = []


def encode_image(url, name=None, **additional_properties):
    processed = face_recognition.load_image_file(open_image.get(url))
    encodings = face_recognition.face_encodings(processed)

    return [
        {
            'name': name or url,
            'url': url,
            'encoding': encoding,
            ** additional_properties
        }
        for encoding in encodings
    ]


def add_known_image(url, **kwargs):
    images = encode_image(url, **kwargs)

    known.extend(*images)

    return known


def test_for_known_faces(url):
    results = []

    for image in encode(url):
        for source in known:
            possible_match = face_recognition.compare_faces(
                [source['encoding']],
                image['encoding']
            )

            if any(possible_match):
                results.append({
                    'name': source['name'],
                    'found_at': url,
                    'image': image,
                    'for': source,
                })

    return results


if __name__ == '__main__':
    pass
