import pytest
import requests
import certifi_icpbr

def test_google():
    # before patching/unpatching, Google cert validation should work with either CA root
    requests.get("https://www.google.com")
    requests.get("https://www.google.com", verify=certifi_icpbr.where())

    # patch, access and unpatch
    certifi_icpbr.patch_requests()
    requests.get("https://www.google.com")
    certifi_icpbr.unpatch_requests()

    # ensure unpatching reverted to original state
    requests.get("https://www.google.com")
    requests.get("https://www.google.com", verify=certifi_icpbr.where())


def test_siscomex():
    # before patching/unpatching, Siscomex cert validation should work only if we include ICP-BR certs
    with pytest.raises(requests.exceptions.SSLError):
        requests.get("https://portalunico.siscomex.gov.br/")
    requests.get("https://portalunico.siscomex.gov.br/", verify=certifi_icpbr.where())

    # patch, access and unpatch
    certifi_icpbr.patch_requests()
    requests.get("https://portalunico.siscomex.gov.br/")
    certifi_icpbr.unpatch_requests()

    # ensure unpatching reverted to original state
    with pytest.raises(requests.exceptions.SSLError):
        requests.get("https://portalunico.siscomex.gov.br/")
    requests.get("https://portalunico.siscomex.gov.br/", verify=certifi_icpbr.where())
