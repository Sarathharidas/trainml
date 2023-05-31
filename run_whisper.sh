#!/bin/bash
usage() {
  # Display the usage and exit.
  echo "Usage: ${0} ENDPOINT_URL IMAGE" >&2
  echo 'Send an image to an endpoint to be classified' >&2
  exit 1
}

if [[ "${#}" -lt 2 ]]
then
  usage
fi

function cross_base64() {
  case "$OSTYPE" in
    darwin*)  base64 -i ${1};; 
    *)        base64 ${1} ;;
  esac
}

ENDPOINT_URL=$1
FILE_NAME=$(basename ${2})

(echo -n "{\"name\": \"${FILE_NAME}\", \"contents\": \""; cross_base64 ${2}; echo '"}') 
#|
#curl -H "Content-Type: application/json" -d @-  ${ENDPOINT_URL}/predict 