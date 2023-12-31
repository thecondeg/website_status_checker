#!/bin/bash

website_check() {
	
	website=$1
	status=$(curl -Is -L --connect-timeout 3 --max-time 6 $website | grep -i '^HTTP'| tail -n 1 | cut -d' ' -f2)
	if [ "$status" == "200" ]; then
		echo "$website is up!"
	else
		echo "$website is down!"
	fi
}

website_array=("www.google.com" "www.notarealwebsite165347.com" "www.facebook.com" "github.com")

for website in "${website_array[@]}"; do
	website_check "$website"
done
