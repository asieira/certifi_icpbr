cheesecake: sdist
	cheesecake_index --path dist/`ls -1 dist/`

README.rst: README.md
	pandoc --from=gfm --to=rst -o README.rst README.md

gencerts:
	./gencerts.sh

sdist: README.rst gencerts
	python setup.py clean
	rm dist/*
	python setup.py sdist

pypi: sdist
	twine upload -r pypi dist/*

pypitest: sdist
	twine upload -r pypitest dist/*
