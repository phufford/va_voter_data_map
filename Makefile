
VENV = venv
VOPT = --python=python3


scrape: $(VENV)
	$(VENV)/bin/python src/selenium_scraper.py

$(VENV): $(VENV)/bin/activate
	$(VENV)/bin/pip3 install -Ur requirements.txt

#http://blog.bottlepy.org/2012/07/16/virtualenv-and-makefiles.html
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || virtualenv $(VENV) $(VOPT)
	touch $(VENV)/bin/activate
