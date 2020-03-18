#!/bin/sh
exec $1 file-server --root `dirname $0`/build/dirhtml --listen :2015

