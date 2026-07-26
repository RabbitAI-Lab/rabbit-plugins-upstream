# Suggestion Contract (optional, minimal)

Use **only after** sources were actually read. For dry-run planning, stay in [search-playbook.md](search-playbook.md).

Prefer plain chat bullets. Use a marker block only if a host requires an interchange format.

## Preferred minimal chat shape

```text
outside-help hint (current response only)
fingerprint: host|version|symptom|constraint_pattern|desired_next_outcome
hint: <one narrow next check>
why: <why it matches this thread>
check: <manual verification>
do_not_apply_when: <when to skip>
evidence:
- primary: <url>
- secondary: <url>
advisory_only: true
transport_scope: current_response_only
```

Rules:

- one primary + one independent non-primary evidence URL
- ≥4/5 fingerprint axes must match
- include `do_not_apply_when` and a manual check
- no durable memory, no next-turn retention fields
- no commands to auto-run

## Optional host markers (legacy-compatible)

```md
<!-- find-community-help:suggestions:start -->
# find-community-help suggestions
advisory_only: true
thread_scope: active_conversation_only
transport_scope: current_response_only
problem_fingerprint: host|version|symptom|constraint_pattern|desired_next_outcome

## suggestion-1
title: <short>
hint: <narrow idea>
manual_check: <how to verify>
do_not_apply_when: <skip when>
evidence:
- primary_official_docs: https://...
- secondary_github_issue: https://...
<!-- find-community-help:suggestions:end -->
```

Legacy `agent-travel` markers may still be accepted by old hosts. New output should use `find-community-help` markers or plain chat.
