#!/bin/bash

set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# show current directory
function show_curr_dir {
    echo "$THIS_DIR"
}