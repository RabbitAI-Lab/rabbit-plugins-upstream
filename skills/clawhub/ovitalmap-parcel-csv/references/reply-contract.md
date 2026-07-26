# OpenClaw Reply Contract

Every pipeline response contains:

```text
status: needs_input | ready | completed | blocked
next_action: machine-readable next step
required_input: exact missing confirmations or values
reply_zh: concise Chinese user-facing response
result: structured evidence and file paths
```

## Agent behavior

- `needs_input`: send `reply_zh`, include relevant coordinate/code preview from `result`, and stop. Ask only for `required_input`.
- `ready`: report the concise result and perform `next_action` when it requires no new user decision.
- `completed`: send `reply_zh`, attach/link all paths in `result`, and identify 顶点表 versus 边界表.
- `blocked`: explain `reply_zh`, make no success claim, and wait for corrected input or retry safely.

Use Chinese by default. Do not expose status keys, run state, or raw JSON unless the user asks for technical details.

## Critical gates

The pipeline must not pass these gates implicitly:

- `confirmed_coordinates`: user verified the displayed WGS84 vertices.
- `country_code`: country/region is known rather than guessed.
- `provider_resolutions.{parcel_ref}`: missing or non-exact provider match is resolved per parcel.
- `duplicate_resolutions.{parcel_ref}`: identical submitted boundaries are confirmed as `same` or `different`.
- `official_id_resolutions.{parcel_ref}`: duplicate official IDs are corrected or cleared.
- `confirmed_codes`: user approved generated codes before Step 3.
- `auto_accept_codes`: explicit permission required only for non-interactive `--step all`.

Use stable parcel refs in decisions:

```json
{"provider_resolutions":{"P01":"中非李总"},"duplicate_resolutions":{"P02":"different"}}
```

Legacy zero-based keys remain accepted as input.

Do not combine multiple unrelated questions. Present all currently missing critical fields once, as a short list, then wait for the user's answer.
