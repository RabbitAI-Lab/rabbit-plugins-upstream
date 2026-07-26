# Trigger Policy

Decide whether outside help is justified. At least one **semantic** signal is required.

## Semantic signals

| Signal | Use when | Mode |
| --- | --- | --- |
| No clear next step | Local inspection produced no plausible next action | `low` |
| Progress stalled | Active task not moving despite reasonable local work | `medium` |
| Repeated local attempts | Same failure/fix path keeps returning | `medium` |
| Reinventing-wheel risk | Maintained library, official recipe, known issue, or mature pattern may exist | `low` |
| Version mismatch | Docs, package, registry, or model memory may be stale | `low` |
| User asks community help | User wants community/official experience for this stuck task | `medium` |
| User asks deep help | User explicitly wants a broader outside pass | `high` |

## Not triggers

- Healthy tasks with a clear next step
- One-shot errors before local checks
- General research, news, pricing, curiosity
- Delivery windows alone: `heartbeat`, `scheduled`, `task_end`, `idle_fallback`

## Conversation mapping (no host state)

Map from the active thread narrative only. Do not invent host scheduling state.

- no next step → no clear next step
- stalled → progress stalled
- same loop → repeated local attempts
- likely known solution → reinventing-wheel risk
- docs/package/registry drift → version mismatch
- user asks help → user community help
- user asks broader pass → user deep help

Without host automation, treat the run as `user_request` / `manual_request`.

## Host automatic windows only

If a host auto-invokes this skill, still require a semantic signal plus:

- no user/agent operation in progress
- no pending tool approval
- active conversation within 24h
- quiet after user (~20m) and agent (~5m)
- rate limits (default: 1/thread/day, 3/user/day)
- same-fingerprint cooldown (~12h) unless user re-asks or a new semantic signal appears

Hosts own scheduling. This skill does not implement a runtime.
