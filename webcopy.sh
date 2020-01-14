#!/bin/sh
# credits go to unix.stackexchange.com/questions/a/6397
find `dirname $0`/build/dirhtml/ -mindepth 1 -maxdepth 1 -exec \
	cp -r -t $1 -- {} +

