export PYTHONPATH=$(shell pwd)

all: deps tests doc

clean:
	make -C docs clean
	-rm .coverage

deps:
	pip install -r requirements.txt

tests:
	py.test \
		--pep8 \
		src
