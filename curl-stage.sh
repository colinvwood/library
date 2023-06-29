#!/usr/bin/env bash

curl \
--include --data token=b1a7627e-f102-444f-863e-6d52867a0ac2 \
--data-urlencode version=2023.2 \
--data package_name=q2-taxa \
--data repository=qiime2/q2-taxa \
--data run_id=4287383941 \
--data artifact_name="osx-64" \
--data build_target=dev \
--header 'Content-Type: application/x-www-form-urlencoded' \
--request POST localhost:8000/api/v1/packages/stage/
