#!/bin/bash
# Mock CRITIC + VERIFIER (review_cmd) — REJECT path (test_04).
#
# REVIEW -> one blocker finding, REQUEST_CHANGES.
# VERIFY -> the finding stays disputed, REJECT. After --max-loops 1 with no
# arbiter the loop terminates REJECTED (exit 3) and records a [REJECTED] commit.
input="$(cat)"
if printf '%s' "$input" | grep -q 'For each finding'; then
    printf '%s\n' '{"results":[{"id":"A1","status":"disputed","evidence":"the placeholder finding cannot be conclusively resolved","confidence":"high","basis":"code"}],"epistemic_distribution":{"confidence":{"high":1,"medium":0,"low":0},"basis":{"spec":0,"code":1,"inference":0,"external":0}},"summary":"0 resolved, 0 rejected, 1 disputed","verdict":"REJECT"}'
else
    printf '%s\n' '{"findings":[{"id":"A1","severity":"blocker","file":"answer.py","line":1,"summary":"impossible","evidence":"cannot be satisfied"}],"verdict":"REQUEST_CHANGES"}'
fi
exit 0
