#!/bin/bash

fswatch -d taoge_blog |(while read;date; echo "*** Realoading ***"; do make html ;done)
