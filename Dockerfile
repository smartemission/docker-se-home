FROM python:2.7.14-alpine

LABEL maintainer="Just van den Broecke <justb4@gmail.com>"

# These are default values,
# Override when running container via docker(-compose)

# General ENV settings
ENV LC_ALL="en_US.UTF-8" \
	LANG="en_US.UTF-8" \
	LANGUAGE="en_US.UTF-8" \
	# WSGI server settings, assumed is gunicorn  \
	CONTAINER_NAME="se_home" \
	CONTAINER_HOST=0.0.0.0 \
	CONTAINER_PORT=80 \
	WSGI_WORKERS=4 \
	WSGI_WORKER_TIMEOUT=6000 \
	WSGI_WORKER_CLASS="sync"

RUN pip install gunicorn flask

# Add entry-script and app to root dir
COPY entry.sh /
ADD app /app

# Make executable
RUN chmod a+x /*.sh

EXPOSE ${CONTAINER_PORT}

ENTRYPOINT /entry.sh
