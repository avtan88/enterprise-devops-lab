IMAGE_NAME=enterprise/python-runtime
VERSION ?= 1.0.1
REGISTRY ?= ghcr.io/avtan88

LOCAL_TAG=$(IMAGE_NAME):$(VERSION)
REMOTE_TAG=$(REGISTRY)/$(IMAGE_NAME):$(VERSION)

build:
	docker build -t $(LOCAL_TAG) .

tag:
	docker tag $(LOCAL_TAG) $(REMOTE_TAG)

push:
	test -n "$(REGISTRY)"
	docker push $(REMOTE_TAG)

publish: build tag push

print:
	@echo "LOCAL_TAG=$(LOCAL_TAG)"
	@echo "REMOTE_TAG=$(REMOTE_TAG)"
