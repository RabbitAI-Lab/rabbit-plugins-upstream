# MagicPay Result States

<!-- magicpay-continuation-contract:v1 -->
## Contents

- [Reading CLI Results](#reading-cli-results)
- [Troubleshooting](#troubleshooting)
- [plan-fill](#plan-fill)
- [apply-fill](#apply-fill)
- [fill-field](#fill-field)
- [Post-submit Result Policy](#post-submit-result-policy)
- [Request Paths](#request-paths)
- [session_stop](#session_stop)
- [Protected Actions](#protected-actions)

MagicPay product work starts from an active session created with
`magicpay start-session`. Browser-dependent states assume a browser child has
been launched or attached inside that product session.

## Reading CLI Results

For MagicPay JSON results, branch on fields, not on prose:

1. `success` — `true` means the command reached its typed success contract;
   `false` means a controlled blocked or failed outcome.
2. `outcomeType` — the command-specific success or blocked class.
3. `error` or `reason` — machine-readable subtype for blocked or terminal
   failure cases.

Use `message` and `reason` as text for the user or timeline. Do not parse them
to discover control flow.

## Troubleshooting

| Symptom | What it means | Next command |
| --- | --- | --- |
| A MagicPay or MagicBrowse result reports a failure the agent cannot recover | Automatic control cannot continue, but page state, approvals, or created links may already be safe and reusable | Tell the user what completed safely, then explain the returned `message`, `reason`, or `finalMessage`; never show a raw stack trace or go silent |
| The result leaves a page, hosted `requestUrl`, or exact remaining manual step | The user has a safe manual path even though automatic control stopped | Hand over that page, link, or exact step |
| The result says `retryable: true` | The command contract permits one retry | Retry once only |
| The result does not say `retryable: true` | An account or configuration fix is required before retry | Do not retry; report the needed fix and stop |
| The result carries `agentInstructions` | The runtime supplied the exact continuation for this state | Follow `agentInstructions` verbatim |

## `plan-fill`

Read `plan-fill` results before calling `apply-fill`; apply only after the
active Memory fill plan is available.

<!-- magicpay-continuation:v1 id=statuses-plan-result-apply action=plan-apply -->
After `magicpay plan-fill`, execute its exact returned `applyCommand`.
<!-- /magicpay-continuation:v1 -->

Success shape:

```json
{
  "success": true,
  "plan": {
    "id": "plan_123",
    "valueVisibility": "handles_only",
    "fields": []
  },
  "nextAction": "apply-fill"
}
```

The plan is value-free. It may contain target refs, Memory field refs, safe
descriptor metadata, and value handles, but not raw saved values.

Blocked shape:

```json
{
  "success": false,
  "outcomeType": "blocked",
  "error": "matcher_unavailable",
  "message": "MagicPay could not complete the semantic Memory matcher request.",
  "reason": "The Memory matcher is unavailable through the current gateway configuration.",
  "nextAction": "ask-user"
}
```

`plan-fill.error` values:

- `browser_connection_failed` — the browser child is unreachable. `nextAction`
is `attach`; rebind the approved browser process before retrying.
- `page_resolution_failed` — the browser is reachable but the current page
  could not be resolved. Refresh or re-observe the browser state.
- `verification_required` — CAPTCHA, anti-bot, or human verification blocks
  planning. Use the CAPTCHA/auth handoff rules; do not retry through it.
- `redirect_loss` — checkout, booking, cart, or upstream redirect context was
  already lost. Stop; do not continue on a contextless page.
- `matcher_unavailable` — the semantic Memory matcher could not run. Fail
  closed and ask the user or retry only after gateway/tooling state changes.
- `match_ambiguous` or `match_unusable` — the model output could not be safely
  validated. Do not guess.
- `workflow_session_required` — there is no active MagicPay product workflow
  session. Start or restore the product session first.

## `apply-fill`

Read `plan-fill` results first, then run exactly its returned `applyCommand`
(`apply-fill`) only for the active Memory fill plan.

<!-- magicpay-continuation:v1 id=statuses-plan-apply action=plan-apply -->
After `magicpay plan-fill`, execute its exact returned `applyCommand`.
<!-- /magicpay-continuation:v1 -->

Success shape:

```json
{
  "success": true,
  "status": "filled",
  "completedLedger": []
}
```

Branch on `success`, then `status`:

- `filled` — planned Memory values were filled. Refresh the browser state and
  continue with the page-control owner. If the next browser action is consequential,
  get matching typed MagicPay approval.
- `page_changed` or `stale_plan` — the live page no longer matches the active
  plan. Rerun `magicpay plan-fill` on the current page before applying again.

`fieldDiagnostics[]` is facts-only. Each entry contains `targetRef`,
display `fieldLabel`, `reasonCode`, `confidence`, and optional redacted `evidence`;
it does not contain a command or remediation field. Use `reasonCode` together
with required/optional field status, visible page context, task risk, and UX
constraints:

| `reasonCode`                                                    | Agent policy                                                                                                                                  |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `target_not_found`, `stale_target`                              | Refresh or re-observe the page, then rerun `plan-fill` and run exactly its returned `applyCommand`.                                           |
| `target_not_writable`                                           | Do not blind replan. Check whether the field is gated by a prerequisite, disabled until user action, optional/skippable, or a stop condition. |
| `memory.missing`                                                | Ask the user or use the active Memory request flow; do not invent a value.                                                                    |
| `memory.conflict`                                               | Ask the user to choose the correct candidate.                                                                                                 |
| `memory.ask_before_use`                                         | Wait for approval or denial before materializing the value handle.                                                                            |
| `provider_needs_reauth`                                         | Treat as stale payment authorization: verify live payment facts and use the typed `authorize-payment` path. Never create a provider reconnect request. |
| `provider_unavailable`                                          | Stop with `payment_method_unavailable`. There is no user provider-connection action; retry only after service state changes and a fresh observation. |
| `projection.invalid_value`, `projection.missing_select_option`  | Ask/update Memory or stop, depending on field criticality and visible allowed options.                                                        |
| `projection.missing_format_hint`                                | Peek or re-observe target details, then refine format hints before retrying.                                                                  |
| `projection.unsupported_shape`, `projection.ambiguous_value`    | Use page-control fallback only when safe; otherwise ask or stop.                                                                              |
| `unsupported_frame`, `unsupported_target`                       | Use page-control fallback only when the target is visible and the action remains value-safe; otherwise stop with the product error.           |
| `magicbrowse_write_failed_uncertain`, `magicpay_internal_error` | Do not claim success. Refresh evidence, apply remaining safe fields, or stop and report the product error.                                    |

Failure shape:

```json
{
  "success": false,
  "error": "active_plan_required",
  "message": "MagicPay could not find an active Memory fill plan.",
  "nextAction": "plan-fill"
}
```

Branch on `reason` and optional `error`:

- terminal `denied`, `expired`, `failed`, or `canceled` — stop the MagicPay
  path and report the exact state.
- `diagnostic_timeout`, `aborted` — the request is still live; resume the exact
  returned `pollCommand` and keep its continuation.
- `server_deadline_overrun`, `client_safety_deadline` — reconcile once with
  `magicpay requests`; if the same request is still overdue, preserve it,
  report the server inconsistency, and stop automatic polling.
- `error: "active_plan_required"` — run `magicpay plan-fill` first.
- `error: "memory_materialization_failed"` — MagicPay could not materialize an
  approved value handle. Surface the blocker without exposing raw values.
- `error: "browser_fill_blocked"` — the browser fill layer refused the fill.
  Treat as blocked; refresh state before any retry.

## `fill-field`

Use `fill-field` only when the higher-automation path missed a field or chose
the wrong target and the agent can point to a specific observed target id. It
accepts one value-free Memory field binding per invocation and returns the same
apply-style result shape as `apply-fill`.

Success or partial shape:

```json
{
  "success": true,
  "status": "filled",
  "completedLedger": [],
  "fieldDiagnostics": []
}
```

Policy:

| Result                                                  | Agent policy                                                                                               |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `filled`                                                | Refresh the browser state and continue from the observed page.                                             |
| `partial`                                               | Inspect `fieldDiagnostics` per field before deciding whether to replan, ask, skip, or stop.                |
| `needs_replan` with `target_not_found` / `stale_target` | Refresh or re-observe, then return to `plan-fill` unless the agent has a new concrete binding.             |
| `blocked` with `target_not_writable`                    | Do not blind replan. Check prerequisite, user unlock, optional status, or stop.                            |
| Memory/provider diagnostics                             | Use the same user, approval, and provider paths as `apply-fill`; do not bypass them through raw values.    |
| Projection diagnostics                                  | Refine `projectionPart` only if the target is visibly a typed part; otherwise ask, skip optional, or stop. |

Failure shape:

```json
{
  "success": false,
  "error": "invalid_product_fill_field_request"
}
```

Never use `fill-field` as the default fill path. Start with `plan-fill`, run
exactly its returned `applyCommand`, and drop to `fill-field` only when the
agent has better observed target evidence than the matcher/planner result.

## Post-submit Result Policy

After any approved form submit, observe the page again before claiming success
or deciding recovery:

- If navigation happened or the page shows a clear confirmation/success state,
  continue from that observed state. For a payment, run
  `magicpay payment-result`; the merchant page alone is not provider-backed
  success.
- If the page remains on the form with field-level validation messages,
  associate each visible error with its field. Treat saved-value errors as a
  possible Memory/provider value problem, but do not guess hidden values. Ask
  the user to update the relevant Memory item, choose another approved item, or
  stop.
- If the page shows only a general form error, stop and report the visible
  reason. Retry only after page, user, Memory, or provider facts change.
- Never claim success from the submit click alone, and never retry blindly on
  merchant validation errors.
- For `payment_initiated` with `nextAction: "await_notification"`, immediately
  tell the user: "Your transfer has been initiated. It can take a few minutes
  to settle. You will receive a MagicPay notification when it is complete."
  Do not run `magicpay payment-result` again, and do not end or cancel the
  session; durable settlement continues in the background.
- For `payment_pending` or `payment_unknown`, keep the workflow open and follow
  the typed `nextAction`: solve a confirmed challenge without pressing Pay,
  run an exact returned `pollCommand` only when present, or stop automatic
  polling on `contact_support` with no poll command. For recoverable payment failure, share the
  returned copy and links, run the exact returned `recovery.pollCommand`, and
  require fresh authorization before any retry.
- `payment_submission_unconfirmed` means local evidence cannot establish a
  provider submission or a safe retry. Follow the returned typed next action,
  never report settlement, and never treat page silence as permission to click
  again.

## Request Paths

- `auto` — MagicPay resolved the request without waiting for a new user
  decision.
- `confirm` — MagicPay paused for explicit approval before using the protected
  data or action path.
- `provide` — MagicPay paused because the user needed to provide missing data
  or select the right item.
- terminal `denied`, `expired`, `failed`, or `canceled` — stop the MagicPay
  path and report the exact state. Polling deadlines are typed non-terminal
  states governed by the canonical loop in `SKILL.md`.

### `session_stop`

A special variant of `canceled`: the whole session was terminated
mid-flow by the user, a trust rule, or the backend. The result includes
`session_stop` details with a `code` and a human-readable `message`.

Do not retry the same request inside the same session. End the session with
`magicpay end-session`, then start a new one if the user wants to continue.

## Protected Actions

- `artifact` — a typed action command completed and returned the request
  artifact. Proceed with exactly that approved action; stop only if page facts
  changed.
- `pending` — a typed action command with `--return-pending` created the
  request, stored `currentRequestId`, and returned `requestUrl`. Give that
  link to the user and immediately run the exact returned `pollCommand`. For
  `authorize-payment`, the user can approve in MagicPay UI with the link or
  provide the OTP they received; if they provide OTP, run the exact returned
  `confirmOtpCommand`, then resume the exact returned `pollCommand`. For
  non-payment actions, use the link only and keep that poll attached.
- `approved`, `executing` — approval is recorded; run the exact returned
  `pollCommand`. Never request approval again. For payment approval,
  `payment_authorization_finalized` is the safe ready signal even if the API
  status remains `executing`. After acknowledging approval detection, do not
  start `magicpay plan-fill`, an `applyCommand`, or long Memory work while the
  poll is merely `approved` or `executing`. Wait until the same attached
  `pollCommand` returns a ready or terminal result. Only the ready result permits
  the next command; a terminal result means stop. The CLI exposes payment
  readiness as `success: true`,
  `outcomeType: "payment_authorization_finalized"`, and
  `nextAction: "continue_checkout"`. This final JSON overrides any earlier
  progress line that merely reported `executing`.
- `otp_invalid`, `otp_expired`, `otp_attempts_exceeded` — the OTP channel
  failed. Report the typed failure without repeating the OTP. While the
  request itself is still pending, keep MagicPay UI approval available.
- `request_already_resolved` — another channel already resolved the same
  pending request. If a terminal request state was returned, treat the request
  as terminal; otherwise continue the exact returned `pollCommand`. Do not
  apply a second decision.
