#!/bin/bash
if [ $# = 0 ] ; then
    echo "USAGE: $0 Title of post"
    exit 1
fi
title="$@"
name=${title// /-}
hugo new "post/$name.md"
sed -e "s/!!!TITLE_HERE!!!/$title/" -i "content/post/$name.md" 
${EDITOR:-vim} "content/post/$name.md"
