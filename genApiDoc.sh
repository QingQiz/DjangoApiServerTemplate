#!/usr/bin/env bash

# remove old api doc
rm -rf ./common/static/common/doc
rm -rf ./static/common/doc

# npm install -g apidoc
apidoc -o ./common/static/common/doc

# replace api-url (http://API-URL) to current url (window.location.origin)
sed -i -e \
	's/"url": "http:\/\/API-URL/"url": window.location.origin + "/g' \
	./common/static/common/doc/api_data.js
sed -i -e \
	's/"http:\/\/API-URL/window.location.origin + "/g' \
	./common/static/common/doc/api_project.js

./manage.py collectstatic --noinput
