#!/bin/bash

fswatch -d source |(while read;do make html;done)
