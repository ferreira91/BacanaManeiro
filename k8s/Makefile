NAMESPACE ?= bacana-maneiro
TAG ?= latest

deploy-namespace:
	kubectl apply -f namespace.yaml

# helm
deploy-dependencies:
	helm upgrade broker stable/rabbitmq --install -n $(NAMESPACE)

install-charts:
	$(MAKE) SERVICE_NAME=gateway install-chart

install-chart:
	helm upgrade $(SERVICE_NAME) charts/$(SERVICE_NAME) --install \
	--namespace=$(NAMESPACE) \
	--set image.tag=$(TAG)
