#!/usr/bin/env bash

rm certifi_icpbr/cacert.pem

set -e

pip install --upgrade certifi
cp `python -c "import certifi; print(certifi.where())"` certifi_icpbr/cacert.pem

mkdir tmp
curl http://acraiz.icpbrasil.gov.br/credenciadas/CertificadosAC-ICP-Brasil/ACcompactado.zip --output tmp/icpbr.zip
cd tmp
unzip -j icpbr.zip
rm icpbr.zip
for f in *.crt; do
    echo -en "\n# $f\n" >> ../certifi_icpbr/cacert.pem
    cat "$f" >> ../certifi_icpbr/cacert.pem
done
cd ..
rm -rf tmp
