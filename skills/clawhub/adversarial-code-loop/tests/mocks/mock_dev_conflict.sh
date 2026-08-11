#!/bin/bash
# Mock BUILDER for the merge-conflict race (test_08): rewrites the tracked
# shared.txt then sleeps a few seconds so the parent branch can advance and
# race the squash-merge. Whether or not a conflict actually fires, the pipeline
# must abort gracefully rather than crash.
cat >/dev/null 2>&1
printf 'loop-change\n' > shared.txt
sleep "${ACL_MOCK_SLEEP:-4}"
exit 0
