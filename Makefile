IMAGES := gateway
TAG ?= dev

install-dependencies:
	pip install -U -e "gateway/.[dev]"
	pip install -U -e "establishments/.[dev]"

build-base:
	docker build --target base -t bacana-maneiro-base .;
	docker build --target builder -t bacana-maneiro-builder .;

build: build-base
	for image in $(IMAGES) ; do TAG=$(TAG) make -C $$image build-image; done





