#!/bin/sh
# This script produce xterm window with a mono-font displayed

FONT_NAME="anonymous pro"

alias b='tput bold'
alias b-='tput sgr0'

sample() {
    echo -e "Showing monospace font: $(b)${FONT_NAME}$(b-)"
    card | duplicate_in_bold
}

duplicate_in_bold() {
    while read line
    do
        echo -e "${line}$(b)${line}$(b-)"
    done
}

card() {
    cat <<EOS
┌←─ ~ ────────────────────────────○[↓]→┐
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
│                                      │
├──────────────────────────────────────┤
└──────────────────────────────────────┘
$                                    [^]
EOS
}

sample

