#!/bin/bash -e

systemd-run \
	--unit=graphite-web-changepassword-${RANDOM}.service \
	"--description=Graphite - Web Application - Change a user's password" \
	--pty \
	--send-sighup \
	--quiet \
	/usr/bin/django-admin changepassword --settings=graphite.settings "${@}"
