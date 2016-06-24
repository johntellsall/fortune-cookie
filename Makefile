all: test

test:
	docker-compose --verbose up

# NOTES
# docker-compose build
# docker  tag 5795e johntellsall/fortunecookie_web
# docker push johntellsall/fortunecookie_web
#
# docker-cloud nodecluster create --sync jm_cluster

# docker-cloud stack create --name fortune
#
# docker-cloud up --sync

terminate-service:
	docker-cloud service ps | awk '/fortune/ {print $$2}' | xargs docker-cloud service terminate

# docker-cloud node ls
