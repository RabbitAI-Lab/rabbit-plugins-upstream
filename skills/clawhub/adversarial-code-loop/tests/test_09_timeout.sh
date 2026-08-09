#!/bin/bash
# test_09 — per-subprocess timeout.
# DEV sleeps longer than --timeout, so the BUILD phase is killed: the build
# result is non-zero and the pipeline reports an infrastructure failure (1).
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec

ACL_MOCK_SLEEP=2 "$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" --timeout 1 \
    --dev-cmd "$MOCKS/mock_dev_slow.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t09.log 2>&1
code=$?
[ "$code" -eq 1 ] || die "expected exit 1 (infra / build timeout), got $code (see /tmp/acl_t09.log)"

note "build subprocess timeout surfaced as exit 1"
exit 0
