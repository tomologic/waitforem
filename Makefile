build:
	python setup.py bdist_wheel --universal

install: build
	cd dist && python -m pip install *.whl

uninstall:
	pip uninstall --yes waitforem

clean:
	rm -rf build dist *.egg-info

test:
	flake8 --verbose --show-source --max-line-length=120 --exclude='build,dist,.git,*.egg-info'
