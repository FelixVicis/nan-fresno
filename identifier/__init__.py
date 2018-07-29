#!/usr/bin/python3
import face_recognition
from .open_image import *

known = []


def encode_image(url, name=None, **additional_properties):
    try:
        processed = face_recognition.load_image_file(get(url))
        encodings = face_recognition.face_encodings(processed)
        image = from_url(url)
    except Exception as e:
        print(e)
        return []

    return [
        {
            'name': name or url,
            'url': url,
            'encoding': encoding,
            'image': image,
            ** additional_properties
        }
        for encoding in encodings
    ]


def add_known_image(url, **kwargs):
    images = encode_image(url, **kwargs)

    known.extend(images)

    return known


def test_for_known_faces(url):
    results = []

    for image in encode_image(url):
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
