#!/bin/bash

set -e
clang -fsanitize=dataflow -o $OUTPUT $CFLAGS $SOURCE $TARGET_DIR/impl.c
$OUTPUT