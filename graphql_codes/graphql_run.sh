#!/bin/bash

set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# show current directory
function show_curr_dir {
    echo "$THIS_DIR/"
}

# run the uvicorn server at localhost 8000
function run_server {
    uvicorn api_backbone:app --reload
}

function run_gql_app_main {
    uvicorn gql-app-main.app.main:app --reload
}

# Check if a function name was provided as an argument
if [[ $# -gt 0 ]]; then
    "$@"
else
    echo "No function name provided. Usage: bash $0 <function_name>"
fi