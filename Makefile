.PHONY: celan build run

APP_NAME=spyglass


clean:
	docker container stop ${APP_NAME} || true
	docker container rm ${APP_NAME} || true
	docker image rm ${APP_NAME} || true

clean-windows:
	docker container stop ${APP_NAME} || (exit 0)
	docker container rm ${APP_NAME} || (exit 0)
	docker image rm ${APP_NAME} || (exit 0)

build:
	docker build -t ${APP_NAME} .

run:
	docker run -it -p 8000:8000 --name ${APP_NAME} ${APP_NAME}