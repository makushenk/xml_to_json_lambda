import xmltodict


def handler(event, context) -> dict:
    try:
        return {
            'status_code': 200,
            'body': xmltodict.parse(event)
        }
    except TypeError:
        return {
            'status_code': 400,
            'error_detail': f'Expected XML string or byte-like object. Got {type(event)} instead.'
        }
    except xmltodict.expat.ExpatError:
        return {
            'status_code': 400,
            'error_detail': f'Invalid XML.'
        }
