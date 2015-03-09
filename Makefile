default: buildout

buildout: bin/buildout
	bin/buildout -c buildout.cfg -N

test:
	bin/test -s plonesocial.microblog
	bin/flake8 src/plonesocial

bin/buildout: bin/python
	bin/pip install -r requirements.txt

bin/python:
	virtualenv --clear --no-site-packages .

buildout-cache/downloads:
	[ -d buildout-cache ] || mkdir -p buildout-cache/downloads

clean:
	rm -rf bin/* .installed.cfg parts/download

