#!/bin/bash

fswatch -d taoge_blog |(while read;do make html;done)
