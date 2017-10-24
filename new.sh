#!/bin/bash
title="$@"
name=${title// /-}
hugo new "post/$name.md"
sed -e "s/!!!TITLE_HERE!!!/$title/" -i "content/post/$name.md" 
${EDITOR:-vim} "content/post/$name.md"
