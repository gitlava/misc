#!/bin/sh

. ./sh.doppelvar

echo Setting 0
sVar Var1 0
echo "Var1    : '$(gVar Var1)'"; echo "Var1__p : '$(pVar Var1)'"

echo Setting 1
sVar Var1 1
echo "Var1    : '$(gVar Var1)'"; echo "Var1__p : '$(pVar Var1)'"

echo Setting 1
sVar Var1 1
echo "Var1    : '$(gVar Var1)'"; echo "Var1__p : '$(pVar Var1)'"

echo Setting "1   0"
sVar Var1 "1   0"
echo "Var1    : '$(gVar Var1)'"; echo "Var1__p : '$(pVar Var1)'"

echo Setting '##$! .'    '.   $$ \$%;;>hh'
sVar Var1 '##$! .'    '.   $$ \$%;;>hh'
echo "Var1    : '$(gVar Var1)'"; echo "Var1__p : '$(pVar Var1)'"

echo Setting "1   0"
sVar Var1 "1   0"
echo "Var1    : '$(gVar Var1)'"; echo "Var1__p : '$(pVar Var1)'"

