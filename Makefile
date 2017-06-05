
VENV = venv
VOPT = --python=python3


scrape: $(VENV)
	mkdir -p data
	$(VENV)/bin/python src/multiscraper.py

build: requirements phantomjs


#http://blog.bottlepy.org/2012/07/16/virtualenv-and-makefiles.html
$(VENV): $(VENV)/bin/activate
requirements: requirements.txt $(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || virtualenv $(VENV) $(VOPT)
	$(VENV)/bin/pip3 install -Ur requirements.txt
	touch $(VENV)/bin/activate


phantomjs-2.1.1.tar.bz2:
	curl -L -o phantomjs-2.1.1.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
phantomjs: include/phantomjs/phantomjs 
phantomjs-2.1.1-linux-x86_64: phantomjs-2.1.1.tar.bz2
	tar -xjf phantomjs-2.1.1.tar.bz2
include/phantomjs/phantomjs: phantomjs-2.1.1-linux-x86_64
	mkdir -p include/phantomjs
	cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs include/phantomjs/phantomjs

