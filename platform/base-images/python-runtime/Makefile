IMAGE_NAME=enterprise/python-runtime
VERSION ?= 1.0.0
ECR ?=

LOCAL_TAG=$(IMAGE_NAME):$(VERSION)
REMOTE_TAG=$(ECR)/$(IMAGE_NAME):$(VERSION)

build:
	docker build -t $(LOCAL_TAG) .

push:
	test -n "$(ECR)"
	docker tag $(LOCAL_TAG) $(REMOTE_TAG)
	docker push $(REMOTE_TAG)

print:
	@echo "LOCAL_TAG=$(LOCAL_TAG)"
	@echo "REMOTE_TAG=$(REMOTE_TAG)"
