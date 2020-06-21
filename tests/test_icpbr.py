import pytest
import requests
import certifi_icpbr

def test_google():
    valid_url = 'https://www.google.com'

    # before patching/unpatching, Google cert validation should work with either CA root
    requests.get(valid_url)
    requests.get(valid_url, verify=certifi_icpbr.where())

    # patch, access and unpatch
    certifi_icpbr.patch_requests()
    requests.get(valid_url)
    certifi_icpbr.unpatch_requests()

    # ensure unpatching reverted to original state
    requests.get(valid_url)
    requests.get(valid_url, verify=certifi_icpbr.where())


def test_siscomex():
    icp_br_only_URL = 'https://www.iti.gov.br/'

    # before patching/unpatching, Siscomex cert validation should work only if we include ICP-BR certs
    with pytest.raises(requests.exceptions.SSLError):
        requests.get(icp_br_only_URL)
    requests.get(icp_br_only_URL, verify=certifi_icpbr.where())

    # patch, access and unpatch
    certifi_icpbr.patch_requests()
    requests.get(icp_br_only_URL)
    certifi_icpbr.unpatch_requests()

    # ensure unpatching reverted to original state
    with pytest.raises(requests.exceptions.SSLError):
        requests.get(icp_br_only_URL)
    requests.get(icp_br_only_URL, verify=certifi_icpbr.where())
