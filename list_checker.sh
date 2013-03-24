#!/bin/sh

# generate semplice.list from the master file

echo -n > semplice.list

for mirror in `cat semplice.list.master`; do
	wget -t 1 $mirror/dists/unstable/main/binary-i386/Packages.gz -O /tmp/test
	if [ "$?" = "0" ]; then
		echo "$mirror" >> semplice.list
	fi
done
