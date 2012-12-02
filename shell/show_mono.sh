#!/bin/sh
# This script produce xterm window with a mono-font displayed

FONT_NAME="anonymous pro"
CUSTOM_TEXT="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

BON=$(tput bold)
BOFF=$(tput sgr0)

NON=$(tput rev)
NOFF=$(tput sgr0)

sample() {
    echo -e "Showing monospace font: ${NON}${FONT_NAME}${NOFF}"
    card | duplicate_in_bold
}

duplicate_in_bold() {
    while read line
    do
        echo -e "${line}${BON}${line}${BOFF}"
    done
}

custom_line_1() {
    printf "%-32s" "$(echo "${CUSTOM_TEXT}" | cut -c 1-32)"
}

custom_line_2() {
    printf "%-32s" "$(echo "${CUSTOM_TEXT}" | cut -c 33-64)"
}

card() {
    cat <<EOS
┌←─ ~ ────────────────────────────○[↓]→┐
│ell 'lL', one '1'                lL1iI│
│little eye 'i', big eye 'I'           │
│Zero '0'                           0oO│
│little oh 'o', big oh 'O'             │
│                                      │
│   \`~!@#$%^&*()_+-=[]\\\\{}|:";'<>?,./   │
│              0123456789              │
│                                      │
│  THE QUICK BROWN FOX JUMPS OVER THE  │
│               LAZY DOG               │
│                                      │
│  the quick brown fox jumps over the  │
│               lazy dog               │
│                                      │
│  Your text here:                     │
│  ╔════════════════════════════════╗  │
│  ║$(custom_line_1)║  │
│  ║$(custom_line_2)║  │
│  ╚════════════════════════════════╝  │
├──────────────────────────────────────┤
└──────────────────────────────────────┘
$                                    [^]
EOS
}

sample

