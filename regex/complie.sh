#!/bin/sh


F_REGEX="${1}"
[ -f "${F_REGEX}" ] || { echo "${F_REGEX}: File not found."; exit 1; }


{ sed 's/\s//g; s/#.*$//;' | sed ':a; N; s/\n//; ta'; } <"${F_REGEX}"

