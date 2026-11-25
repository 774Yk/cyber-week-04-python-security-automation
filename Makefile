.PHONY: test lint security scan

test:
	python -m unittest discover -s tests -v

lint:
	python -m compileall -q secauto tools tests
	python -m py_compile secauto/*.py tools/*.py tests/*.py

security:
	python tools/security_checks.py

scan:
	python -m secauto.cli sample-data
