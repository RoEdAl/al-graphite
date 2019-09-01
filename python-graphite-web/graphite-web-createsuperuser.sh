#!/bin/bash -e

systemd-run \
	--unit=graphite-web-createsuperuser-${RANDOM}.service \
	'--description=Graphite - Web Application - Create/update a superuser with password' \
	--pty \
	--send-sighup \
	--quiet \
	/usr/bin/django-admin createsuperuser --settings=graphite.settings "${@}"
