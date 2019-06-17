|PyPI version| |Build Status|

.. _certifi--icp-brasil:

certifi + ICP Brasil
====================

This package is meant to act as a drop-in replacement to
`certifi <https://pypi.org/project/certifi/>`__ for use with
`requests <https://pypi.org/project/requests/>`__ that includes all of
the same Mozilla root CA certificates, but also includes all of the ICP
Brasil root CAs made available
`here <https://www.iti.gov.br/repositorio/84-repositorio/489-certificados-das-acs-da-icp-brasil-arquivo-unico-compactado>`__.

The reason why this package exists is that for regulatory and political
reasons, many Brazilian government websites use the country-specific
`ICP Brasil <https://www.iti.gov.br/icp-brasil>`__ certification scheme,
which is not distributed by default by major browsers and operating
system distributions. This causes a lot of problems for developers that
need to programatically interact with those services.

This is an example of the sort of issue you'll encounter by default:

::

   >>> import requests
   >>> requests.get('https://portalunico.siscomex.gov.br/')
   Traceback (most recent call last):
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/connectionpool.py", line 603, in urlopen
       chunked=chunked)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/connectionpool.py", line 344, in _make_request
       self._validate_conn(conn)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/connectionpool.py", line 843, in _validate_conn
       conn.connect()
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/connection.py", line 370, in connect
       ssl_context=context)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/util/ssl_.py", line 355, in ssl_wrap_socket
       return context.wrap_socket(sock, server_hostname=server_hostname)
     File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py", line 412, in wrap_socket
       session=session
     File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py", line 853, in _create
       self.do_handshake()
     File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py", line 1117, in do_handshake
       self._sslobj.do_handshake()
   ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/requests/adapters.py", line 449, in send
       timeout=timeout
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/connectionpool.py", line 641, in urlopen
       _stacktrace=sys.exc_info()[2])
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/urllib3/util/retry.py", line 399, in increment
       raise MaxRetryError(_pool, url, error or ResponseError(cause))
   urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='portalunico.siscomex.gov.br', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)')))

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/requests/api.py", line 75, in get
       return request('get', url, params=params, **kwargs)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/requests/api.py", line 60, in request
       return session.request(method=method, url=url, **kwargs)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/requests/sessions.py", line 533, in request
       resp = self.send(prep, **send_kwargs)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/requests/sessions.py", line 646, in send
       r = adapter.send(request, **kwargs)
     File "/Users/asieira/.virtualenvs/certifi_icpbr/lib/python3.7/site-packages/requests/adapters.py", line 514, in send
       raise SSLError(e, request=request)
   requests.exceptions.SSLError: HTTPSConnectionPool(host='portalunico.siscomex.gov.br', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)')))

Usage
-----

The recommended way of using this package is to take advange of the
``verify`` parameter used throughout
`requests <https://pypi.org/project/requests/>`__ to allow the default
root CAs file to be overridden:

::

   >>> import requests
   >>> import certifi_icpbr
   >>> requests.get('https://portalunico.siscomex.gov.br/', verify=certifi_icpbr.where())
   <Response [200]>

Alternatively, it is possible to monkey-patch
`requests <https://pypi.org/project/requests/>`__ so that it uses this
package's root CAs file by default. *This is risky and can stop working
in future versions
of*\ `requests <https://pypi.org/project/requests/>`__, so it is
strongly recommended you use the first approach if possible. This is the
same example using that approach:

::

   >>> import certifi_icpbr
   >>> certifi_icpbr.patch_requests()
   >>> import requests
   >>> requests.get('https://portalunico.siscomex.gov.br/')
   <Response [200]>

.. |PyPI version| image:: https://badge.fury.io/py/certifi-icpbr.svg
   :target: https://badge.fury.io/py/certifi-icpbr
.. |Build Status| image:: https://travis-ci.org/asieira/certifi_icpbr.svg?branch=master
   :target: https://travis-ci.org/asieira/certifi_icpbr
