import os
import sys

def where():
    f = os.path.dirname(__file__)
    return os.path.join(f, 'cacert.pem')

def patch_requests():
    if 'requests' not in sys.modules:
        import requests
    req = sys.modules['requests']
    req.certs.where = where
    req.utils.DEFAULT_CA_BUNDLE_PATH = where()
    req.adapters.DEFAULT_CA_BUNDLE_PATH = where()
    sys.modules['requests'] = req

def unpatch_requests():
    if 'requests' not in sys.modules:
        return
    cert = sys.modules['certifi']
    req = sys.modules['requests']
    req.certs.where = cert.where
    req.utils.DEFAULT_CA_BUNDLE_PATH = cert.where()
    req.adapters.DEFAULT_CA_BUNDLE_PATH = cert.where()
    sys.modules['requests'] = req
