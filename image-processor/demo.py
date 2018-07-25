rs_make_wish = 'http://colorado.wish.org/~/media/009-000/Wish%20Photos/I%20wish%20to%20meet/Jilian%20-%20Rebecca%20Sugar/648%20x%20444%20MAW_EDITED_JILLIAN_GOLZ_HIGHRES-978.ashx?bc=d1e9fa&h=444&w=648'
random_crowd = 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Crowd_shot_-_Flickr_-_Al_Jazeera_English.jpg'
rb_va_crew = 'http://www.latimes.com/resizer/G3v3JaM_ywTroY02iDXVX_xJie8=/1400x0/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/3AMOC46ZRJC7LLO47TQFIP454I.jpg'

rb_rolling_stones = 'https://www.rollingstone.com/wp-content/uploads/2018/06/rs_lead_rachelsugar-0eb09ebb-0250-4f53-9cdf-b700ac8c3aa3.jpg'
su_solo = 'https://vignette.wikia.nocookie.net/steven-universe/images/f/f0/Steven_Shield_WD.png/revision/latest/scale-to-width-down/350?cb=20160406110631'

scan = [
    rs_make_wish,
    random_crowd,
    rb_va_crew
]

photos = [
    rb_rolling_stones,
    su_solo,
]

known = []
found = []

import face_recognition
import open_image


def encode(url, name=None):
    processed = face_recognition.load_image_file(open_image.get(url))
    encodings = face_recognition.face_encodings(processed)

    return [
        {
            'name': name or url,
            'url': url,
            'encoding': encoding
        }
        for encoding in encodings
    ]


def test(url):
    results = []

    for image in encode(url):
        for source in known:
            possible_match = face_recognition.compare_faces([source['encoding']], image['encoding'])

            if any(possible_match):
                results.append({
                    'name': source['name'],
                    'found_at': url,
                    'image': image,
                    'for': source,
                })

    return results


def s1():
    for photo in photos:
        for encoding in encode(photo):
            known.append(encoding)


def s2():
    for photo in scan:
        for encoding in test(photo):
            found.append(encoding)


def s3():
    print('Scanned {} photos'.format(len(scan)))
    print('Found {} match'.format(len(found)))
    print('\t', '\n\t'.join(['{} at {}'.format(e['name'], e['found_at']) for e in found]))


s1()
s2()
s3()
