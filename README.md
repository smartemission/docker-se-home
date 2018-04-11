# Smart Emission Home Web App

Home/landing page web app for the SE platform.

## Hosting

The Docker Image is hosted as: 
[smartemission/se-home at DockerHub](https://hub.docker.com/r/smartemission/se-home).

It is accessed/viewed via `*.smartemission.nl`, e.g. https://pdok.smartemission.nl.

## Environment

The following environment vars need to be set, either via `docker-compose` or
Kubernetes.

|Environment Variable|Default
|---|---
|HERON_LOG_LEVEL|10 (debug)

## Architecture

The image contains a simple Flask webapp running in gunicorn WSGI server.
The app runs the Home static webpages for now, but can be expanded in future
with more dynamic info.

## Links

* SE Platform doc: http://smartplatform.readthedocs.io/en/latest/
