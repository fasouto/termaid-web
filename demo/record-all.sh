#!/bin/bash
# Record every tape one at a time (parallel runs make the termaid hook time out).
cd "$(dirname "$0")"
for t in claude-*.tape; do
  echo "== $t"; vhs "$t" 2>&1 | tail -1
done
