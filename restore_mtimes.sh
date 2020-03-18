#!/bin/bash

# credits for idea go to
# https://stackoverflow.com/questions/22497597/get-the-last-modification-data-of-a-file-in-git-repo

shopt -s globstar
for i in source/**/*.rst source/*.rst; do
	MTIME="$(git log -1 --pretty="format:%ci" "$i")"
	echo "$i" "$MTIME"
	touch -md "$MTIME" "$i"
done

