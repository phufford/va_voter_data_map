
VENV = venv
VOPT = --python=python3


scrape: $(VENV)
	$(VENV)/bin/python src/selenium_scraper.py

requirements: requirements.txt

venv/lib/python3.6/site-packages/selenium: $(VENV)
	$(VENV)/bin/pip3 install -Ur requirements.txt

#http://blog.bottlepy.org/2012/07/16/virtualenv-and-makefiles.html
$(VENV): $(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || virtualenv $(VENV) $(VOPT)
	touch $(VENV)/bin/activate

phantomjs-2.1.1.tar.bz2:
	curl -L -o phantomjs-2.1.1.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2


phantomjs-2.1.1/bin/phantomjs: phantomjs-2.1.1.tar.bz2
	tar -xjf phantomjs-2.1.1.tar.bz2

phantomjs: phantomjs-2.1.1/bin/phantomjs
