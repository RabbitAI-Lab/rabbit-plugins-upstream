# MagicPay Command Guide

<!-- magicpay-continuation-contract:v1 -->
## Contents

- [Setup And Readiness](#setup-and-readiness)
- [Native Payment Operations](#native-payment-operations)
- [MagicSearch Discovery](#magicsearch-discovery)
- [Product Session And Browser Child Control](#product-session-and-browser-child-control)
- [Memory Fill](#memory-fill)

The hard rules from `SKILL.md` apply to every current command: protect the
MagicPay API key and CDP endpoint, use only the browser process approved for
this task, keep Memory fill to plan/apply without final submission, and get
the matching typed MagicPay approval before any submit, protected action,
purchase, login, identity submission, account change, or other consequential
action.

For every command that returns `requestHandoff`, follow the canonical One
User-Request Loop in `SKILL.md`. The returned `pollCommand` is the authority;
do not reconstruct it, shorten it, or create a replacement request.

## Setup And Readiness

### `magicpay init <apiKey> [--api-url <url>] [--env <name>]`

Save the API key to the MagicPay config file. By default this is
`~/.magicpay/config.json`; when `MAGICPAY_HOME` is set, it is
`$MAGICPAY_HOME/config.json`. When `--api-url` is provided, `init` also stores
the gateway base URL there. Omit `--api-url` for normal setup; the CLI uses
its bundled default MagicPay gateway URL. Pass `--api-url <url>` only for a
non-default staging, self-hosted, or test gateway. Use `--env` together with
`--api-url` to persist a development or local profile. Hosted links always
print the production web origin regardless of profile.

Do not print, log, or share the API key or the persisted config. If this
machine or workspace is shared or compromised, ask the user to rotate or
revoke the key before continuing.

### `magicpay setup start --email <email> --platform <runtime> [--agent-name <name>] [--api-url <url>] [--env <name>]`

Start first-time MagicPay account bootstrap from an agent chat. Use this only
for the landing/bootstrap setup path when there is no local MagicPay gateway
config yet. The command sends a one-time code to the user and returns a signed
challenge for `setup verify`.

Do not use this command for prompts copied from the authenticated MagicPay UI.
Those prompts already include a setup token and should use `magicpay init`.

### `magicpay setup next [--intent landing] [--platform <runtime>] [--agent-name <name>] [--api-url <url>] [--env <name>]`

Return natural-language setup instructions for the current agent. Use this as
the first command after the MagicPay skill is installed from the landing
bootstrap path. The result includes:

- `instructions` — the text the agent should follow and/or say next;
- `state` — a compact debug/test label, not a prompt mapping key;
- `agent` and `gateway` metadata when a matching connection already exists.

Follow `instructions` directly. Do not maintain a separate `state` /
`nextAction` mapping in the skill or prompt. Production setup must pass the
production API and environment explicitly:

```bash
magicpay setup next --intent landing --platform codex --agent-name "Codex Agent" --api-url https://durcottggsiesxxqzvbb.supabase.co/functions/v1/api --env production
```

When a local or development setup prompt supplies a complete profile, use
only those explicit override values instead:

```bash
magicpay setup next --intent landing --platform codex --agent-name "Codex Agent" --api-url <branch-api-url> --env local
```

### `magicpay setup verify --challenge <challenge> --otp <otp> --platform <runtime> [--agent-name <name>] [--api-url <url>] [--env <name>]`

Complete first-time setup after the user provides the OTP. The command creates
or reuses the user's MagicPay account, creates or reuses the agent, and stores
the resulting gateway config locally.

Every successful verification returns `nextAction: "payment-balance"`, including
`created`, `existing`, and backwards-compatible `unknown` account statuses.
Continue with the balance-driven flow in the previously returned `setup next`
instructions. Do not use `account.status` to decide whether the user needs a
top-up link.

Do not print, log, or summarize OTP digits, raw API keys, or the persisted
config. If verification fails, show the safe command error and ask before
retrying.

### `magicpay status`

Check CLI health, authenticated identity, and update state. Use this as the
normal preflight command before a MagicPay Memory fill task.

### `magicpay doctor`

Inspect the local config file when `status` still fails after `init`.

### `magicpay --version`

Print the installed CLI version.

### `magicpay --help`

Print the installed CLI command surface. Use this when a command is missing or
when the skill was installed from a local AgentPay dist path. The first-time
setup flow requires `setup next` to appear in help output before continuing.

### `magicpay top-up-link`

Generate a hosted card top-up link for the configured MagicPay agent. During
landing setup, run this only after `magicpay payment-balance` without asset
flags returns the authoritative unified contract with an integer-string
`available` exactly equal to `"0"` and the `setup next`
instructions request it. This rule applies equally to new and returning
accounts. It may also be used when the user explicitly asks to top up.
Share the exact hosted URL and say, localized naturally: “Top up your MagicPay
balance through this link: {exact hosted top-up URL}. Crypto top-ups can take a
few minutes to arrive. MagicPay will notify you when the funds are available.”
Render the returned URL as the link target; never print the placeholder. Do not
append a final-payment approval reminder to this top-up handoff.

Hosted links always open on the production web app; swap the domain by hand
for local admin testing. Use `--hosted-base-url` only as an explicit
one-command diagnostic override. For normal use, run plain
`magicpay top-up-link`.

### `magicpay top-up-address [--asset <symbol>]`

Request direct crypto top-up addresses from MagicPay without creating a hosted
top-up link. With no selector, return every method in the structured `methods`
array. With `--asset USDT` or `--asset USDC`, return only that asset's method;
do not ask the user to choose a network when the result contains one network.

Present each exact `address` together with `asset`, `network`, and
`networkLabel`, localized to the user's language. Tell the user to send only
that asset on that network. Do not show `operationId`, `requestKey`, or internal
retry fields unless troubleshooting requires them.

If the result contains `unavailable`, do not hide it. Present successful
methods, explain unavailable choices briefly, and use only the exact returned
`retry.command` for a same-request retry. Never construct or change
`--request-key` yourself. An address is not proof of a deposit; wait for the
funding operation and unified Ledger settlement.

This command is independent from `magicpay top-up-link`. Run both only when the
user explicitly asks for both surfaces.

### `magicpay card-balance [--card-id <id>]`

Read the compatibility balance attached to one issued MagicCard through the
configured agent API key. Do not use this as the customer's MagicPay balance,
for setup completion, or for a payment spend check. Use parameterless
`magicpay payment-balance` for those unified-balance decisions. This
compatibility lookup is read-only and does not require a product session or a
payment approval.

If it fails with a missing API key, run `magicpay status`, then use
`magicpay setup next` as the setup recovery branch selector. Do not ask for the
user's email unless the returned setup `instructions` ask for it. If it fails
with a 403, the local key is not agent-scoped or is no longer linked to this
account.

### `magicpay list-cards`

List issued MagicCards available to the linked MagicPay account. Use this only
for read-only account/source checks. Do not use it to reveal full card details;
provider-backed card handles still require the normal MagicPay payment-card
authorization flow during checkout.

### `magicpay card-transactions [--card-id <id>] [--limit <n>] [--page <n>]`

List recent provider card transactions for the linked MagicCard. This is a
read-only history lookup through the agent API key.

### `magicpay recent-transactions [--limit <n>]`

List recent MagicPay workflow transactions for this agent. Use this when the
user asks for recent MagicPay activity, recent purchases, or transaction
history rather than provider card ledger rows.

## Native Payment Operations

### `magicpay payment-balance`

Read `magicpay.total-balance/v1`, the authoritative unified MagicPay customer
balance. Use its `available` quantity as the sole spend check for x402, crypto,
and card payments. The backend owns rail selection, inventory, and conversion.

### `magicpay payment-balance --asset-namespace <value> --asset-id <value> --network <value>`

Read a diagnostic exact-asset projection for one supported tuple. This is useful
for funding and operational inspection, but it is not customer spend authority.
Never block a payment because this rail-specific projection is zero when the
unified balance is sufficient.

### `magicpay funding-address --idempotency-key <key> --asset-namespace <value> --asset-id <value> --network <value>`

Request the QWIKWallet funding address for one exact asset and network. Reuse
the same idempotency key for the same funding intent; do not manufacture a new
address to work around a pending deposit. Present the returned address together
with its exact asset and network, and refresh the unified balance only after the
operation or Ledger projection confirms funding. This is not the hosted
MagicCard `top-up-link` flow.

### `magicpay direct-transfer --session <id> --idempotency-key <key> --asset-namespace <value> --asset-id <value> --network <value> --principal <integer> --maximum-debit <integer> --destination <value>`

Start one direct-transfer operation in the dedicated payment/crypto intent
session. Require exact user-intended amount, asset, network, destination, and
maximum debit. Convert display values with exact string arithmetic, verify
the no-selector unified `available >= maximumDebit`, and reuse the same
idempotency key for every replay or recovery of this user intent.

This command creates the operation-backed approval request. Run `magicpay
requests`, share its exact request URL when present, and execute the exact
returned poll command. Do not call browser-checkout `authorize-payment`, create
a second approval, or replace a pending or ambiguous transfer.

### `magicpay x402-purchase --session <id> --idempotency-key <key> --maximum-debit <integer> ((--resource-url <url> [--resource-method GET]) | (--resource-url <url> --resource-method POST --resource-body '<json>') | --selection-ref <ref>)`

Start or replay one HTTP-native x402 purchase in the exact payment intent
session. Verify the unified payment balance, then preserve the same session,
idempotency key, seller resource or selection, and maximum debit. Do not supply
or require a customer Base-USDC balance: the server freezes the seller
requirement and resolves settlement inventory behind the unified balance.
GET is the default direct-resource method. Use POST only when the seller's
trusted contract supplies the exact JSON body; POST requires `--resource-body`,
and GET or MagicSearch selection forbids it.

Run `magicpay requests --session <id>`, share the exact returned request URL,
and keep the returned request and operation identities together.

<!-- magicpay-continuation:v1 id=x402-operation-approval-poll action=run-exact-returned-attached field=pendingRequest.pollCommand -->
Immediately run the exact returned `pendingRequest.pollCommand` and remain attached to that process.
<!-- /magicpay-continuation:v1 -->

### `magicpay x402-purchase-result --operation-id <operationId>`

Read the paid resource only after that same operation is terminal `completed`.
An approval, HTTP response, pending operation, or treasury submission is not a
result. Never retrieve a result for another operation or expose payment headers,
signing material, or internal treasury references.

The result is bounded and integrity-checked by MagicPay. Decode its Base64 body
according to `mediaType`: parse JSON for `application/json`, present bounded
UTF-8 for `text/*`, and for binary or unknown media show safe metadata without
dumping raw Base64 into chat. Preserve `resultRef`, `sha256`, and `expiresAt` in
the completion summary.

### `magicpay payment-operation <operationId>`

Read the same durable operation. Branch on structured `state`, `nextAction`,
and `retry.mode`; approval, reservation, provider submission, and callback HTTP
success are not settlement. A `reserved` balance is the in-flight maximum debit
and `available` is spendable.

### `magicpay reconcile-payment-operation <operationId>`

Reconcile only when `nextAction` or a retryable error explicitly directs it.
Keep the same session, operation id, and idempotency key. Never reconcile by
creating a replacement send. Only terminal `completed` proves settlement;
denial, expiry, cancellation, and definitive failure end that attempt.

## MagicSearch Discovery

### `magicsearch query "<refined prompt>" [options]`

Resolve a purchase, booking, merchant, provider, checkout, or product intent to
a URL before ordinary web search or browser navigation. Use this when the user
has asked to buy, book, reserve, order, or compare something but has not given a
specific checkout URL.

`magicsearch` uses the same MagicPay gateway config as `magicpay`. Run
`magicpay status` first; if MagicPay is healthy but `magicsearch` is missing,
repair it from the same install source as the MagicPay CLI. For local AgentPay
setup, install both `magicsearch-local.tgz` and
`magicsearch-cli-local.tgz` with the other local dev tarballs. Include
`magicbrowse-cli-local.tgz` whenever browser automation may be needed; the
`magicbrowse-local.tgz` library tarball does not install the `magicbrowse`
binary. For public installs, use `npm i -g @nuanu-ai/magicsearch-cli@latest`.

Use JSON output so the agent can inspect provider metadata and fallback state:

```bash
magicsearch query "<refined purchase prompt>" --choice-policy never --json
```

The closed query shape for normal purchase discovery is
`magicsearch query "<refined prompt>" --choice-policy never --json`. Add only
the query hints documented below. Keep currency inside the refined prompt, not
in a `--currency` option; that option belongs to `magicsearch discover`.

Inspect `source`, `searchProvider`, `fallbackReason`, and `provider` in the
JSON. `source: "exa"` or `searchProvider: "exa"` means MagicSearch's Exa
fallback produced the target; use that URL before falling back to MagicBrowse
or ordinary browser search. Only switch to MagicBrowse/browser fallback when
MagicSearch fails, blocks, or returns no usable URL.

MagicSearch provider selection is automatic. Do not ask the user to choose
between providers, MCP tool profiles, or entries such as Google Flights versus
Apify. If a provider choice appears, rerun discovery with
`--choice-policy never` and continue with the automatically selected result.

### `magicsearch discover "<refined prompt>" [options]`

Resolve the target provider and run supported provider-side discovery before
browser handoff. Use this for Google Flights/Fli when the user asks for a
flight and has provided enough route/date facts. Start a MagicPay product
workflow first so multiple itineraries can become a tokenized UI choice:

```bash
magicpay start-session "<short task name>"
magicsearch discover "<refined purchase prompt>" --category flights --origin DPS --destination SIN --departure-date 2026-07-12 --json
```

One live MagicPay session resolves automatically; with several parallel
sessions, add `--session <sessionId>` (or export `MAGICPAY_SESSION`) using the
id printed by `magicpay start-session`.

Required flight slots:

- `--origin <IATA>`
- `--destination <IATA>`
- `--departure-date <YYYY-MM-DD>`

Useful optional flight slots:

- `--return-date <YYYY-MM-DD>`
- `--cabin-class <class>`
- `--passengers <n>`
- `--currency <code>`
- `--country <code>`
- `--language <code>`
- `--max-stops <mode>`
- `--sort-by <mode>`

If the result is `status: "choice_required"`, the options are user-facing
itineraries returned by provider execution. Share `requestUrl`, then poll with
the returned `pollCommand` — it embeds the session:
`magicsearch choose --request <requestId> --session <sessionId> --json` —
until the UI choice resolves.
If the result is `status: "resolved"`, use the returned `url`; for Fli this is
a provider-returned Google Flights booking/search URL. If Fli returns no safe
booking URL, do not synthesize one and do not silently open the generic
provider URL.

Use server-side choice only when more than one actual user-facing purchase
option would make a material difference to the user, such as itineraries,
hotels, rooms, seats, tickets, plans, or comparable checkout offers. This
requires an active MagicPay product session because the choice request
is stored server-side and can be resolved through either the MagicPay UI link
or the CLI. Do not use `choose-target --choice-policy always` to create travel
choices; that command can expose provider/search-target choices before provider
execution.

If the result is `status: "choice_required"`, present the choice both ways,
always:

1. Share the returned `requestUrl` link.
2. Duplicate every entry of the returned `options` array in chat as a numbered
   list with its important details — title, subtitle, price, and any
   distinguishing characteristics (duration, stops, departure/arrival times,
   room type). Never share only the link: the user must be able to decide
   without opening it. Tell the user they can reply with a number here or pick
   in the link.

Then immediately run the returned `pollCommand` or the equivalent command below
and wait for the selected URL. Do not stop after sharing the link and do not
ask the user to come back to chat after choosing in the UI:

```bash
magicsearch choose --request <requestId> --json
```

That command polls the server-side choice request until the user completes the
tokenized MagicPay UI request or the request times out. If it times out while
the user is still deciding, tell the user the choice link is still pending and
rerun the same command.

If the user replies with a number (or otherwise names an option) in chat,
submit the backend-owned id of that option — `options[n-1].id` for a reply of
`n` — instead of continuing to poll:

```bash
magicsearch choose --request <requestId> --choice <choiceId> --json
```

Both resolution paths are equivalent; whichever happens first wins.

Do not choose by list position or label. Use the exact returned `choiceId`.
Do not silently choose for the user; an agent may recommend an option, but the
selection must be explicit.

Useful hints:

- `--merchant <name>`
- `--domain <domain>`
- `--product <name>`
- `--category <name>`
- `--country <code>`
- `--region <region>`
- `--place <place>`
- `--choice-policy auto|always|never`
- `--choice-limit <n>`
- `--choice-mode wait|return-pending|none`
- `--hosted-base-url <url>` one-command override of returned link origins (diagnostics only)

Before querying, extract the user-provided slots and preserve them exactly.
For flights and other directional bookings, keep origin and destination as
separate facts; do not send a natural-language query that can reverse the
route.

Example:

```bash
magicsearch query "buy flight tickets from Denpasar to Singapore on August 1" --category flights --country ID --choice-policy never --json
```

If `magicsearch query` returns `provider.methodType: "mcp"` and
`execution.mcp.profile: "fli"` for a flight search, do not open the generic
provider URL yet; run `magicsearch discover` with the extracted flight slots.
If MagicSearch returns an HTTP `url` from Exa/search fallback, or provider
execution returns a concrete booking/search URL, use it as the browser handoff
target before any MagicBrowse fallback. If MagicSearch returns
`choice_required` for a provider/tool-profile choice, do not show it to the
user; rerun with `--choice-policy never`. If it returns `choice_required` for
actual user-facing purchase options, share `requestUrl` and poll with
`magicsearch choose --request <requestId> --json` until the UI choice resolves,
then use the selected URL. If MagicSearch returns no usable URL, asks for
disambiguation without creating a request, or fails because the gateway is
unavailable, ask the user for the missing choice or explicitly fall back to
ordinary search. Do not silently skip MagicSearch.

## Product Session And Browser Child Control

### `magicpay start-session [name] [--merchant-name <name>]`

Start the MagicPay product session. This is the parent operation for
normal MagicPay product work; it creates the product workflow before any
browser child is required.

`start-session` attempts to cancel/clear a stale previous workflow binding
before it creates the new product session. If that recovery is still blocked,
start manual recovery with `magicpay status`, then either `magicpay
end-session` or a fresh `start-session`.

### `magicpay launch [url] [--profile <name>]`

Launch a browser child inside the active MagicPay product session.

Use this after `magicpay start-session` when MagicPay should create the
browser execution resource. The optional URL places the new browser child at
the starting page. The browser child does not replace the product workflow
identity.

The success result includes the child's `cdpUrl`. Use it when a
page-control tool (for example `magicbrowse attach`) should drive the
same browser inside the workflow; keep the endpoint private.

### `magicpay attach <cdp-url> [--provider <name>]`

Attach an already running browser as the browser child inside the active
MagicPay product session.

Use only a private CDP endpoint for the browser process the user approved for
this task. Treat the endpoint as sensitive because it inherits the browser's
logged-in state. Run `attach` after `start-session` when MagicPay is not yet
bound to the approved browser child, or when the CDP endpoint changed.
Re-attaching the same endpoint is allowed but is not required as a ritual.

### `magicpay browser-status`

Inspect the browser child bound to the active MagicPay product workflow.

This is a browser-dependent diagnostic command. Browser-only state is not
enough; the command requires an active product workflow and a matching browser
child binding.

### `magicpay close`

Close or clear the browser child bound to the active MagicPay product
workflow.

This does not end the product session. Use it when the browser child
should be cleaned up or replaced, then continue the same product workflow with
another `launch` or `attach` if needed.

### `magicpay solve-captcha [--timeout <s>]`

Solve a confirmed CAPTCHA on the current browser child inside the active
MagicPay product workflow.

Only call this when a real CAPTCHA is confirmed present. The command uses the
current bound browser child, and does not close or recreate the browser. Treat
the challenge as cleared only when the result has `fullyResolved: true`,
`merchantCleared: true`, and `outcomeType: "resolved"`. `solverVerified` alone
is progress, not merchant clearance. `success: true` with `fullyResolved: false` or
`outcomeType: "partial"` is not clearance: do not mark the CAPTCHA resolved,
or commit. If the challenge appeared after a final commitment click, continue
the exact returned `payment-result` reconciliation; even a fully resolved solve
does not authorize another click. Otherwise, after a fully resolved solve, get
fresh visible page state from the current page-control owner. Do not invent or run a
page-state CLI such as `magicbrowse get-page-state`; that command is not
documented. Obtain fresh visible state only through the existing page-control
owner's documented continuation. If an old checkout plan is involved, rerun
`magicpay plan-fill` and execute its exact returned `applyCommand` before
resuming. No `magicpay observe` command is documented in this bundle. CAPTCHA
clearance alone does not authorize `magicpay commit`;
commit only at the normal matching-approval and current-live-facts boundary.
When a partial result includes `renderedStateAssessment`, follow its exact
`agentInstructions`. `active` or `uncertain` preserves manual continuation;
`cleared` requires fresh re-observation and reconciliation without claiming
that the CAPTCHA is still visible. No visual assessment authorizes Pay or a
retry.
If the next step is through MagicBrowse, call
`magicbrowse mark-captcha-resolved`, then continue with `magicbrowse act
"continue..."`.
For a manually completed challenge that followed a dispatched final click,
make `magicpay payment-result` the first observer after
`magicbrowse mark-captcha-resolved`; do not run another browser action or press
Pay first.

### `magicpay payment-result`

Read the provider-linked payment result for the active workflow after the
merchant submit attempt. Do not infer payment success from a confirmation page
alone.

Also run this command for post-click `commitment_blocked_by_challenge`,
`commitment_no_observable_effect`, `commitment_clicked_unverified`, and
`commitment_post_click_unreadable` outcomes. Those states are
submission-uncertain, not proof of non-submission. A provider transaction in a
terminal failure, pending, or success state proves that the final click reached
the provider and blocks an automatic recommit.

```bash
magicpay payment-result
```

- `payment_succeeded`: provider-backed success is confirmed. The workflow can
  be ended with the observed amount, currency, merchant, and
  `--payment-outcome provider_confirmed --payment-provider-status success`.
- `payment_initiated` with `nextAction: "await_notification"`: immediately tell
  the user: "Your transfer has been initiated. It can take a few minutes to
  settle. You will receive a MagicPay notification when it is complete." Do
  not run `magicpay payment-result` again, and do not end or cancel the session;
  durable settlement continues in the background. A new unrelated task in the
  same chat may run unscoped `magicpay start-session`, which creates a separate
  lane. With multiple live lanes, scope later commands with the exact
  `--session <intentSessionId>` returned for that lane.
- `payment_pending` or `payment_unknown`: follow the typed `nextAction`. For
  `solve_challenge`, resolve the current challenge without pressing Pay and
  run `payment-result` again. Run a returned `pollCommand` only when present.
  For `contact_support` with no poll command, stop automatic polling and
  request review. Do not retry or report success.
- `payment_failed_recoverable` or `payment_ambiguous`: share the returned
  `userMessage` and `recovery.recoveryRequestUrl` with the user, include
  `recovery.topUpUrl` when returned, then immediately run
  the exact returned `recovery.pollCommand`.
- `payment_failed_terminal`: report the safe returned reason and do not retry
  automatically.

Recovery choices are top up when applicable, retry with fresh authorization,
continue manually at a safe merchant URL, or cancel. A retry must start a new
provider reservation and a fresh `authorize-payment` approval; it must never
reuse the prior authorization. If the selected choice is cancel, `wait-request`
ends the workflow with terminal status `error` and the canonical failure
reason.

### `magicpay end-session`

Complete the active product session and product root run.

Optional completion flags are `--amount-total <number>`, `--currency <code>`,
`--merchant-name <name>`, `--payment-outcome <outcome>`, and
`--payment-provider-status <status>`. Payment outcomes are
`merchant_confirmed` and `provider_confirmed`; provider statuses are `unknown`,
`pending`, and `success`. Cancellation flags are `--cancel` and `--hard-cancel`.
Terminal payment-failure flags are `--fail --payment-failure-reason <reason>`;
normal recoverable failures must stay open through `payment-result` instead.

This is workflow completion only. After it succeeds, return page control to the
page-control owner. A browser tool or orchestrator that launched an owned
disposable browser may clean up its own session when the overall task is done;
an external/user-owned browser stays open unless the user explicitly approves
teardown. `end-session` does not require a live browser child.

When the final purchase amount, currency, or merchant is visible, include it:

```bash
magicpay end-session --amount-total 237.20 --currency SGD --merchant-name KLM
```

If a fresh post-submit observation shows that the merchant accepted the
checkout, record that result without claiming provider settlement:

```bash
magicpay end-session --amount-total 5 --currency USD --merchant-name "Beach Talk Radio" --payment-outcome merchant_confirmed --payment-provider-status pending
```

Use the actual provider state observed through MagicPay. If it was not checked,
use `unknown`; if the provider transaction is pending, preserve `pending`. Use
`--payment-outcome provider_confirmed` only together with
`--payment-provider-status success` after an actual provider-backed success
observation.

Use `--amount` and `--merchant` as aliases only when needed. Do not invent a
price. If a payment webhook later confirms the actual card charge, MagicPay
updates the session with the settled amount separately; `end-session`
still does not submit or authorize payment. A merchant-confirmed result can
complete the workflow while the provider transaction remains pending.

If the user explicitly cancels, aborts, stops, or abandons the flow, or if
cleanup is blocked by a hung approval request while canceling, run:

```bash
magicpay end-session --cancel
```

This sends a canceled terminal status to MagicPay and hard-cancels unresolved
waiting, approved, or executing requests for the workflow. Do not use `--cancel`
for ordinary network timeouts, browser disconnects, or a successful purchase:
those can still have an active user approval in progress. Do not combine
`--cancel` with amount/currency/merchant completion flags.

## Memory Fill

### `magicpay plan-fill`

Run `magicpay plan-fill` before `magicpay apply-fill` to plan Memory field fill
from the active browser page. The command observes the current page, fetches
value-free Memory descriptors from MagicPay, asks the Memory matcher for
semantic target matches, validates the model output, and stores a short-lived
fill plan in the active workflow. Optional usage:
`magicpay plan-fill --planner-hint <text>`. Use the hint only for short
human-readable context about the current form.

Do not pass target matches, Memory catalogs, raw values, materializers, browser
writers, or page target lists. The plan result must remain handles-only. If the
Memory matcher is unavailable, fail closed and report the blocked state instead
of guessing.

If `plan-fill` returns `nextAction: "apply-fill"` or
`memoryRequestHandoff.status: "requires_apply_fill"`, run exactly the returned
`applyCommand` before reporting a missing-Memory blocker to the user.
`plan-fill` does not create hosted Memory request links; `apply-fill` creates
the tokenized `requestUrl` plus `pollCommand`/`resumeCommand` when a missing
passenger, contact, login, identity, or payment value must be collected.
Do not say that MagicPay failed to generate a secure request link based only on
the `plan-fill` result.

### `magicpay list-memory-items --url <current-url> [--status <status>]`

List value-free Memory item metadata for the current site scope. Use
`--all-sites` instead of `--url` only for explicit global Memory review or
editing. The command returns item ids, labels, statuses, read-only markers, and
field refs with labels/hints, never raw values.

### `magicpay list-memory-items --all-sites [--status <status>]`

List value-free Memory item metadata across sites. Use this only for explicit
global review or editing, not as the default page-fill path.

### `magicpay get-memory-item --item-id <itemId>`

Get one value-free Memory item by stable item id. Use it when a prior list
result identified the item that needs inspection before editing.

### `magicpay delete-memory-item --item-id <itemId>`

Soft-delete one editable Memory item by stable item id. Do not delete
provider-backed read-only items.

### `magicpay create-memory-item --item-label <label>`

Create a new Memory item. Add fields with UX-first shortcuts:

```bash
magicpay create-memory-item \
  --item-label "Airline login" \
  --site airline.example \
  --text "Login email=ada@example.com" \
  --secret-text "Password=correct-horse"

magicpay create-memory-item \
  --item-label "Traveler profile" \
  --person "Full name=Ada Lovelace" \
  --date "Date of birth=1815-12-10" \
  --phone "Phone=+14155550100" \
  --secret-phone "Backup phone=+14155550101"
```

Create shortcuts use `"Label=value"` because the fields are new and have no
`fieldRef` yet. Use `--text` for ordinary direct fill, `--date` for
`YYYY-MM-DD`, `--phone` for E.164 phone numbers such as `+14155550100`, and
`--person` for a full name. The `--secret-*` variants set the same value type
with secret display/logging metadata.

### `magicpay add-memory-field --item-id <itemId> --label <label> --value <value>`

Add exactly one field to an existing editable item:

```bash
magicpay add-memory-field \
  --item-id mem_airline_login \
  --label "Recovery code" \
  --value "123456" \
  --secret true \
  --hint "One-time recovery code"
```

Optional flags are `--type text|date|phone_number|person_name`, `--secret
true|false`, and `--hint <text>`. `--type text` means ordinary untyped direct
fill.

### `magicpay update-memory-field --field-ref <fieldRef>`

Update one existing editable field by stable `fieldRef`:

```bash
magicpay update-memory-field --field-ref field_phone --value "+14155550101"
magicpay update-memory-field --field-ref field_phone --secret true
magicpay update-memory-field --field-ref field_phone --type text
magicpay update-memory-field \
  --field-ref field_password \
  --label "Account password" \
  --hint "Account password"
```

Existing fields are never addressed by label. List or get Memory first, choose
the intended `fieldRef`, then update that ref. `--secret true|false` is mutable
display/logging metadata for any field, including phone fields. It is not
encryption and not a value type. `--type text` clears semantic value type.

### `magicpay correct-memory-field --field-ref <fieldRef> [--hosted-base-url <url>]`

Correct one existing field during an active browser fill without putting the
replacement value in the agent command or chat:

```bash
magicpay correct-memory-field --field-ref field_country
```

Open the returned `requestUrl` and submit the replacement through the secure
relay. The same submission updates the exact editable field and permits the
new item revision for the current merchant/session. Poll with the exact returned
`pollCommand`, then run exactly its returned `resumeCommand`. The command requires a current
`plan-fill`, fails closed for missing/ambiguous/read-only refs, and has no
`--value` option. Use direct `update-memory-field` only for explicit Memory
management outside an active protected fill.

<!-- magicpay-continuation:v1 id=commands-memory-correction action=poll-before-resume -->
Run exactly the returned `pollCommand` before exactly the returned `resumeCommand`.
<!-- /magicpay-continuation:v1 -->

### `magicpay delete-memory-field --field-ref <fieldRef>`

Remove one existing editable field by stable `fieldRef`:

```bash
magicpay delete-memory-field --field-ref field_recovery_code
```

If a `fieldRef` is unknown or duplicated, field-level commands fail closed with
a structured CLI error and do not mutate Memory.

Raw JSON is an advanced service/debug escape hatch only:
`magicpay create-memory-item --raw-item-json <json>` and `magicpay
update-memory-item --item-id <itemId> --raw-item-json <json>`. Do not use it as
the normal agent path.

When MagicPay Memory has a provider-backed payment card but the active
session has not been authorized for payment-card reveal, `plan-fill`
keeps the plan value-free and reports machine state instead of card handles:

```json
{
  "kind": "payment_card.authorization_required",
  "category": "payment_card",
  "status": "authorization_required",
  "reason": "payment_authorization_required",
  "blocking": false
}
```

The CLI also adds a diagnostic warning explaining that the card exists and
requires payment authorization before reveal. If the card is needed for the
current payment, collect `amount`, `currency`, `recipient`, `country`, optional
`description`, and optional `recurring`. Follow the closed normal-checkout
shape under `magicpay authorize-payment`; keep country in the comparison record outside the command, never add `--country`, and keep missing live facts unknown until the checkout supplies them. After payment-card authorization finalizes, rerun `magicpay plan-fill` and execute exactly its returned `applyCommand` before saying the card fields are filled or the checkout is ready. Never write, show, or execute a hand-written or sample `magicpay apply-fill`, `magicpay wait-request`, or `magicpay wait-memory`; use only exact returned command fields. Do not ask the user for raw card
details and do not bypass this through lower-level Memory or materialization
calls.

### `magicpay apply-fill`

Run `magicpay plan-fill`, then run exactly its returned `applyCommand` for
`apply-fill`; apply
only the active Memory fill plan. Memory request form links always
open on the production web app; swap the domain by hand for local admin
testing. Use `--hosted-base-url` only for a one-command diagnostic
override. The command refreshes the
browser page state, materializes only the approved values needed by the plan,
writes the planned fields through the browser bridge, and stops before final
commitment actions.

If the result is `status: "waiting_for_user"`, follow its structured action.
For `hosted_request`, give `requestUrl` to the user and immediately poll with
the exact returned `pollCommand`. The link opens the same request functionality as the web-admin
request modal, but as a tokenized agent-flow page where the user can provide
and optionally save the missing Memory value. When `wait-memory` returns
`memoryReady: true`, run exactly the returned `resumeCommand` so MagicPay
claims the protected artifact and fills the
merchant page. Do not use `magicpay wait-request` for Memory request links,
because Memory fulfillment artifacts can contain protected values.

For `chat_question`, ask the exact returned question and pipe the user's answer
only to the exact returned `replyCommand`. For `memory_confirmation`, run the
returned allow or deny command after the user's answer. For `memory_choice`,
show safe labels only and run the command attached to the selected label.
Secret, login, identity, payment, provider-managed, and unknown-sensitivity
fields never use these ordinary chat actions.

After a successful fill, refresh the visible page state through the browser
owner and continue from that state. Use typed action approval before any final
Pay, Book, Send, Submit, login, identity submission, account change, or other
consequential action.

### `magicpay fill-field --field-ref <fieldRef> --target <target> [--item-ref <itemRef> | --item-id <id>] [--projection-part <part>]`

Use `fill-field` only as a lower-automation recovery step after `plan-fill` /
`apply-fill` missed a field or matched the wrong target. One invocation fills
one explicit value-free Memory field into one currently observed browser
target:

```bash
magicpay fill-field --field-ref field.email --target 1
magicpay fill-field --field-ref field.email --target 1 --item-ref mem_profile
magicpay fill-field --field-ref field.birth_date --target 2 --projection-part year
```

Use `--item-ref` or `--item-id` to narrow the Memory item when needed,
`--field-ref` to select the field, and `--target` for the current observed
browser target. `--target` accepts the bare observed id such as `1` or the
canonical ref such as `selector:1`; prefer the bare id from observation output.
Do not invent refs; if the target evidence is stale, re-observe or rerun
`plan-fill` instead.

The command fetches the current Memory catalog, resolves each assignment to a
backend value handle, refreshes current target state, validates approval,
provider, target writability, and projection constraints, then writes through
the same browser bridge as `apply-fill`. It returns the same apply-style shape:
`status`, `fields`, `fieldDiagnostics`, and `completedLedger`.

Optional `projectionPart` is allowed for explicit typed recovery: `year`,
`month`, `day`, `country_code`, `national_number`, `given`, `family`,
`segment_1`, `segment_2`, `segment_3`, or `segment_4`. Unsupported parts return
projection diagnostics.

Do not use `fill-field` as the default fill path, do not pass raw values, and
do not pass target lists, Memory catalogs, materializers, or browser writers.

### `magicpay choose-memory --choice <choiceId>`

Choose one backend-owned Memory candidate returned by `apply-fill` and continue
the active fill plan. Do not choose by number or label in the CLI contract.

### `magicpay memory-reply --request <requestId> --plan <planId>`

Use only the exact `replyCommand` returned by a `chat_question` action. Send the
user's raw answer through stdin, never as an argument. The command maps only
request-bound ordinary fields with the assistive model, submits the canonical
`provided` decision with `save:false`, claims it, and continues applying the
fill. An empty safe mapping falls back to a hosted link for the same request.

### `magicpay authorize-payment --amount <number> --currency <code> --recipient <name> [--description <text>] [--recurring <true|false>] [--authorization-ref <ref>] [--item-ref <vaultItemId>] [--return-pending] [--hosted-base-url <url>]`

Request approval for a payment authorization through the structured
`authorize_payment` action contract.

Use only the options in the heading signature or an exact command returned by
MagicPay. Never synthesize a CLI option from a payment-fact name. Country is a
required matching fact, not an `--country` option.

For a normal live checkout, use this closed normal-checkout shape:
`magicpay authorize-payment --amount <live amount> --currency <live currency> --recipient <live recipient> [--description <live description>] [--recurring <live boolean>] --return-pending`.
Keep `country: <live country>` in a comparison record outside the command.

Before calling it, collect these visible transaction facts from the current
checkout/review page and the user's task:

- `amount` — final amount in major units as a JSON number, not cents and not a
  formatted string.
- `currency` — explicit three-letter currency code.
- `recipient` — merchant or payee the user believes they are paying.
- `country` — visible checkout or billing country; it must match the task and
  remain unchanged through commit.
- `description` — optional short order, plan, subscription, or purpose summary.
- `recurring` — optional boolean; ask the user if recurring status matters and
  is unclear.

`--item-ref` remains the existing Memory item selector. It is not placed in
`params`, and this command does not change how MagicPay discovers or selects
Memory items.

After successful approval, continue with that exact payment: protected payment
artifact use, payment form fill, and final Pay/Submit are covered while
`amount`, `currency`, `recipient`, `recurring`, and country stay unchanged. Stop and ask
again if any of those facts change.

Always use `--return-pending`. It creates the same pending request, stores
`currentRequestId`, and returns the request handle plus `requestUrl` and
`pollCommand`. Without it the command blocks for the full request lifetime
while the user has no way to answer: MagicPay's own notification goes to push
or Telegram, which cannot address a terminal runtime, so relaying `requestUrl`
yourself is the only delivery the user gets. Give the user the returned link,
then immediately run the exact returned `pollCommand`. Do not ask
the user to tell you after approving; `wait-request` observes the same terminal
decision whether it comes from the link, admin, mobile app, or another MagicPay
UI. For payment approvals, tell them they can approve in MagicPay UI with the
link or send the one-time code from the MagicPay email. The active MagicPay
profile supplies the local or hosted-development origin automatically.

A `wait-request` timeout does not mean the user failed to approve. When the
result carries `approvalRecorded: true` (or a `lastObservedStatus` of
`approved` or `executing`), the approval is already recorded and MagicPay is
finalizing it with the payment provider. Run the exact returned `pollCommand` again and
continue; never create a second approval request for a payment already in
flight, and never ask the user to approve again.

### `magicpay sessions`

List the local payment sessions and which one commands resolve to. Run this
whenever a command reports that several sessions are active, instead of
guessing or searching earlier output for a session id. Each entry carries
`sessionId`, `status`, `live`, `hasBrowserSession`, `activeRunId`,
`currentRequestId`, and `autoSelected`; the result also carries
`autoSelectedSessionId`, `selectorRequired`, and a `hint`.

Pass `sessionId` as `--session`. `activeRunId` is run telemetry and is never a
valid selector; passing it returns an error naming the session id to use.

This command is account-level, so it keeps working while session-scoped
commands are refusing to guess.

### `magicpay requests`

Show what the active session is waiting on. The result carries
`intentSessionId` and either `pendingRequest: null` or the blocking request's
`requestId`, `type`, `status`, `title`, `summary`, `expiresAt`, and
`resolutionHint`. When recovery can safely classify the request,
`pendingRequest` also carries its exact recovered `requestUrl`, `pollCommand`,
optional `confirmOtpCommand`, optional `resumeCommand`, `requestHandoff`, and
`agentInstructions`.

If a payment approval finalized after watcher output was lost, the result has
`pendingRequest: null` and `readyRequest` with
`outcomeType: "payment_authorization_finalized"` and
`nextAction: "continue_checkout"`. Treat that recovered ready result as
authoritative and continue checkout; do not poll or authorize again.

Run `magicpay requests` when `authorize-payment`, `end-session`, or another
command is refused because a request is already in progress, or when producer
or poller output was lost. If `pendingRequest.pollCommand` is present, share
the returned `pendingRequest.requestUrl` when present, immediately run the
exact returned `pendingRequest.pollCommand`, and remain attached to that
process. Preserve both the returned `intentSessionId` and
`pendingRequest.requestId`; never create a second request to work around the
first. When present, run the exact returned
`pendingRequest.confirmOtpCommand` only if the user chooses the advertised OTP
channel, then resume the exact returned `pendingRequest.pollCommand`. When
present after Memory becomes ready, run the exact returned
`pendingRequest.resumeCommand`. If `recoveryUnavailable` is returned, follow
the safe `resolutionHint` and do not guess a command. `end-session --cancel`
ends a session regardless of a pending request when the work is genuinely
being abandoned.

<!-- magicpay-continuation:v1 id=requests-recovered-poll action=run-exact-returned-attached field=pendingRequest.pollCommand -->
Immediately run the exact returned `pendingRequest.pollCommand` and remain attached to that process.
<!-- /magicpay-continuation:v1 -->

### `magicpay sign-message --item-ref <walletItemId> --message <text> [--return-pending] [--hosted-base-url <url>]`

Request approval to sign one exact wallet message with the selected wallet
item. Use this for wallet message signing only. After approval, sign exactly
that message; stop and ask again if the message changes.

Use `--return-pending` for link-based handoff. Give the returned `requestUrl`
to the user and immediately run the exact returned `pollCommand`. OTP is not
supported for sign-message requests. The active MagicPay profile supplies the
local or hosted-development origin automatically.

### `magicpay confirm-action --summary <text> [--details <text>] [--return-pending] [--hosted-base-url <url>]`

Request approval for a non-payment consequential action that has no more
specific typed command. Use a concise summary that names the visible action;
add details when the page context, recipient, account, or consequences need to
be explicit.

Use this only for consequential actions without a dedicated typed MagicPay
command. Payments use `authorize-payment`; wallet message signing uses
`sign-message`.

Use `--return-pending` for link-based handoff. Give the returned `requestUrl`
to the user and immediately run the exact returned `pollCommand`. OTP is not
supported for non-payment confirmation requests. The active MagicPay profile
supplies the local or hosted-development origin automatically.

### `magicpay confirm-otp --otp <digits> [--session <id>] [--request <id>]`

Confirm the active pending runtime request by OTP. Run the exact returned
`confirmOtpCommand` only when a pending handoff advertises the `otp` channel
and the user provides that request's OTP. Current payment-approval handoffs are
the eligible path. By default the command uses the active session and
`currentRequestId`; `--session` and `--request` are recovery selectors.

Do not repeat the OTP in chat, summaries, logs, saved notes, or command
reports. OTP success is not request or payment success: immediately continue
the exact returned `pollCommand`. If OTP is invalid, expired, or exhausted,
report that typed failure and keep MagicPay UI approval available while the
request itself remains pending.

### `magicpay wait-request [--session <id>] [--request <id>]`

Resume waiting for the active pending runtime request and claim its result
when it reaches a terminal result. Run the exact returned `pollCommand` after
either MagicPay UI approval or OTP confirmation, and immediately after sharing
any pending typed-action `requestUrl`. The poll covers decisions made through the public
link, admin, mobile app, or any other MagicPay UI for the same server-side
request. The command uses the shared three-second `follow_request` poll and
safe 15-second heartbeats. It continues through `approved` and `executing`,
and clears matching continuation only after a terminal result,
finalized-payment ready signal, or session stop. Diagnostic timeout, caller
abort, host interruption, expiry overrun, and the client safety deadline
preserve the same handoff. Run the exact returned `pollCommand`; after either safety
deadline reconcile once with `magicpay requests` and report if the same
request is still overdue.

After acknowledging approval detection, do not start `magicpay plan-fill`, an
`applyCommand`, or long Memory work while the poll is merely `approved` or
`executing`. Wait until the same attached `pollCommand` returns a ready or
terminal result. Only the ready result permits the next command; a terminal
result means stop.

For `authorize_payment`, the ready result is explicit: `success: true`,
`outcomeType: "payment_authorization_finalized"`, and
`nextAction: "continue_checkout"`. Treat that final JSON as authoritative even
if an earlier progress line in the same command reported `executing`; stop
polling and continue checkout.

Do not use `wait-request` for Memory request links from `apply-fill`, because
those fulfilled artifacts may contain protected values. Memory handoffs return
a `wait-memory` `pollCommand`; run that exact returned `pollCommand` instead.

### `magicpay wait-memory [--session <id>] [--request <id>] [--plan <planId>]`

Poll a pending MagicPay Memory request without claiming protected values. After
sharing an `apply-fill` Memory blocker's `requestUrl`, run the exact returned
`pollCommand`. When it returns `memoryReady: true`, run exactly the returned `resumeCommand` so
`apply-fill` claims the protected artifact internally and fills the merchant
page without printing the values. It has the same three-second poll,
heartbeats, interruption recovery, and safety bounds as `wait-request`, but
must never claim the fulfilled artifact itself.
