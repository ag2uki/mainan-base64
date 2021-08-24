import base64

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    splitted = req.split('base64,')
    if len(splitted) > 1:
        return base64.b64decode(splitted[1])
    else:
        return base64.b64decode(req)
