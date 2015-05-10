#!/bin/bash

make clean
make html

cd ../blog
python -m SimpleHTTPServer 8000
