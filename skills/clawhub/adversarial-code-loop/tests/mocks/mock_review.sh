#!/bin/bash
# Mock CRITIC + VERIFIER (review_cmd) — APPROVE path.
#
# REVIEW and VERIFY share this one command; we distinguish them by the prompt
# the orchestrator emits (the persona prefix never removes these markers):
#   * VERIFY prompt contains "For each finding"
#   * REVIEW prompt otherwise
#
# REVIEW -> one minor finding, REQUEST_CHANGES (forces a FIX round).
# VERIFY -> that finding resolved, APPROVE (loop approves after one fix).
input="$(cat)"
if printf '%s' "$input" | grep -q 'For each finding'; then
    printf '%s\n' '{"results":[{"id":"A1","status":"resolved","evidence":"answer.py contains the requested implementation","confidence":"high","basis":"code"}],"epistemic_distribution":{"confidence":{"high":1,"medium":0,"low":0},"basis":{"spec":0,"code":1,"inference":0,"external":0}},"summary":"1 resolved, 0 rejected, 0 disputed","verdict":"APPROVE"}'
else
    printf '%s\n' '{"findings":[{"id":"A1","severity":"minor","file":"answer.py","line":1,"summary":"trivial","evidence":"placeholder finding"}],"verdict":"REQUEST_CHANGES"}'
fi
exit 0
