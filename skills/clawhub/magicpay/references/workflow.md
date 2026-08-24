# MagicPay Operating Guide

<!-- magicpay-continuation-contract:v1 -->
## Contents

- [One User-Request Loop](#one-user-request-loop)
- [Runtime Routing Details](#runtime-routing-details)
- [Preflight And CLI Health](#preflight-and-cli-health)
- [Purchase Discovery With MagicSearch](#purchase-discovery-with-magicsearch)
- [Start From The Product Session](#start-from-the-product-session)
- [CAPTCHA Recovery](#captcha-recovery)
- [Fill Recovery Ladder](#fill-recovery-ladder)
- [Memory Fill Recovery](#memory-fill-recovery)
- [What MagicPay Stores](#what-magicpay-stores)
- [Payment Authorization Facts](#payment-authorization-facts)
- [Recovery Sequence For Changed Fill Plans](#recovery-sequence-for-changed-fill-plans)
- [Multiple Sensitive Fields](#multiple-sensitive-fields)
- [After end-session](#after-end-session)
- [When To Stop](#when-to-stop)

This reference expands the main skill with the practical rules for running a
MagicPay product workflow. The product session is the parent; browser
launch or attach is a child resource inside that active session.

## One User-Request Loop

Every server-side user request follows one loop. Use the commands returned in
`requestHandoff`; they already contain the exact session and request ids.

| User request | Answer channels | Poller | Fulfilled continuation |
| --- | --- | --- | --- |
| Payment approval (`authorize_payment`) | Secure `requestUrl`, or OTP only when `approvalChannels` includes `otp` | exact returned `pollCommand` | Continue the exact approved payment |
| Other action approval, wallet signature, subscription, or manual handover | Secure `requestUrl` only | exact returned `pollCommand` | Continue the exact approved action |
| Protected Memory data, missing secrets, or candidate/form resolution | Secure `requestUrl` only | exact returned `pollCommand` | Run exactly the returned `resumeCommand`; only `apply-fill` may claim values |
| MagicSearch purchase choice | Secure `requestUrl`, or a safe displayed option chosen in chat | returned `magicsearch choose ...` | Continue with the selected URL |
| Payment-recovery or other MagicPay choice | Secure `requestUrl` only | exact returned `pollCommand` | Execute the returned typed next action |

For payment approval, tell the user: approve with the secure MagicPay link, or
send the one-time code from the MagicPay email. If the handoff returns
`confirmOtpCommand` and the user chooses OTP, run the exact returned
`confirmOtpCommand` without echoing, logging, retaining, or summarizing the
digits, then immediately run the exact returned `pollCommand`. OTP confirmation
is not payment success.
Never invite OTP for a handoff that does not return `confirmOtpCommand`.

After sharing the returned `requestUrl`, immediately run the exact returned
`pollCommand` and remain attached to that process. Once it reports approval
detected, send a short user-visible acknowledgement. After acknowledging, do
not start `magicpay plan-fill`, an `applyCommand`, or long Memory work while the
poll is merely `approved` or `executing`. Wait until the same attached
`pollCommand` returns a ready or terminal result. Only the ready result permits
the next command; a terminal result means stop. Acknowledgement is not
settlement.

<!-- magicpay-continuation:v1 id=request-loop-approval-watch action=run-exact-returned-attached field=pollCommand -->
Immediately run the exact returned `pollCommand` and remain attached to that process.
<!-- /magicpay-continuation:v1 -->

The loop is always:

```text
share link -> run exact returned pollCommand now -> keep that process ->
pending/interrupted means run exact returned pollCommand again ->
lost output means recover once with magicpay requests ->
run exact returned pendingRequest.pollCommand -> remain attached with same request identity ->
request safety bound means reconcile once and report if still overdue ->
stop on server terminal, finalized-payment ready, session stop, or cancellation
```

The SDK polls every three seconds by default and emits a safe heartbeat every
15 seconds. Keep a background process attached and collect its output; do not
replace it with repeated short-lived waits. A diagnostic timeout, caller
abort, host interruption, server-deadline overrun, or client safety deadline
is not denial and must not create a replacement request. Run the exact returned
`pollCommand` again, except after a request safety bound: reconcile once with
`magicpay requests --session <sessionId>`, report a still-overdue server
request, and stop automatic polling. Browser work returns before this
standalone request poll begins, so a browser-action deadline must never be used
as the request's lifetime.

In runtimes that merge stdout and stderr into one transcript, pass `--quiet`
to `magicpay` only when parsing otherwise fails. This does not relax the
attached-poll or user-acknowledgement rules, and quiet output is not evidence
that the request stopped.

Use server-side MagicSearch choice only when the choices are actual
user-facing purchase options, such as itineraries, hotels, rooms, seats,
tickets, plans, or comparable checkout offers. Do not use
`choose-target --choice-policy always` to create travel choices; that command
can expose provider/search-target choices before provider execution.

When `magicsearch discover` or another provider execution result is
`status: "choice_required"`, give the returned `requestUrl` and render its safe
`options` as a numbered list with the important returned details. The user may
choose through the link or reply with a number. Immediately run the returned
`pollCommand` or the equivalent command below and wait for the selected URL.
Do not stop after sharing the link and do not ask the user to come back to chat
after choosing in the UI:

```bash
magicsearch choose --request <requestId> --json
```

That command follows the One User-Request Loop until the user completes the
tokenized MagicPay UI request or a typed safety bound requires reconciliation.

If you display the safe `options` titles/prices/URLs in chat and the user
chooses in chat instead of the UI, submit the backend-owned id:

```bash
magicsearch choose --request <requestId> --choice <choiceId> --json
```

Do not silently pick a MagicSearch choice for the user. You may recommend an
option, but the selected `choiceId` must come from an explicit user choice or
the user completing the tokenized MagicPay request link.

If a MagicSearch response asks the user to choose between providers or tool
profiles, do not surface that provider choice. Rerun the discovery with
`--choice-policy never` and continue with the automatically selected target.

For flight, hotel, and other travel discovery, MagicSearch may select an MCP
provider method backed by a hosted tool profile. Do not bypass that method with
generic web search while it is available. If `magicsearch query` returns
`provider.methodType: "mcp"` and `execution.mcp.profile: "fli"`, run
`magicsearch discover` with structured flight slots instead of launching the
generic Google Flights URL. Only hand off to the browser after provider
execution returns a concrete booking/search URL, or when MagicSearch used
Exa/search fallback because no provider URL was available. Treat a
MagicSearch result with `source: "exa"` or `searchProvider: "exa"` as a valid
MagicSearch handoff target, not a reason to open MagicBrowse first. If the MCP
execution returns multiple viable travel options, use the MagicSearch/MagicPay
choice flow and let the user pick; do not call booking-detail or
checkout-resolution tools for every option before the user chooses.

## Runtime Routing Details

When the user asks the agent to buy, book, reserve, order, or compare something
but has not provided a specific checkout URL, use MagicSearch first. Default
web search is a fallback only when MagicSearch is unavailable, blocked, or
cannot produce a usable target. Let MagicSearch run its provider-index lookup
and Exa/search fallback before switching to MagicBrowse, default web search,
or another browser/page-control fallback. Provider selection is an
implementation detail: do not ask the user to choose between MagicSearch
providers, MCP tool profiles, or entries such as Google Flights versus Apify.
For target discovery, route automatically:

```bash
magicsearch query "<refined purchase prompt>" --choice-policy never --json
```

For supported discovery providers, run the provider execution path before
browser handoff. For Google Flights/Fli, extract IATA route/date slots and let
MagicSearch create the itinerary choice from actual flight results:

```bash
magicpay start-session "<short task name>"
magicsearch discover "<refined purchase prompt>" --category flights --origin DPS --destination SIN --departure-date 2026-07-12 --json
```

One live MagicPay session resolves automatically. When several sessions run in
parallel, pass the session id printed by `magicpay start-session` explicitly —
either `export MAGICPAY_SESSION=<sessionId>` for the rest of the task or
`--session <sessionId>` on each `magicsearch` command; ambiguity is an error,
never a silent guess.

If any command reports several active sessions, do not guess and do not dig
through earlier output: run `magicpay sessions`. It lists every local session
with its status and says which one commands resolve to. Use its `sessionId`
as the `--session` selector — never `runId`, which is telemetry.

To see what a session is waiting on, run `magicpay requests`. It names the
blocking request, its type, and the exact command that resolves it. When a
command is refused because another request already blocks the session, that
error now names the blocker too — run `magicpay requests`, then execute the
exact returned `pendingRequest.pollCommand` when present rather than creating a
second request.

<!-- magicpay-continuation:v1 id=runtime-routing-recovered-poll action=run-exact-returned-attached field=pendingRequest.pollCommand -->
Immediately run the exact returned `pendingRequest.pollCommand` and remain attached to that process.
<!-- /magicpay-continuation:v1 -->

## Preflight And CLI Health

Before the first MagicPay task in a session, run `magicpay status`
and handle the output:

- **Missing or invalid API key.** Ask the user for the key, run
  `magicpay init <apiKey>`, then rerun `magicpay status`.
- **CLI capability mismatch.** Run `magicpay --help` when a skill references a
  command that the installed binary does not recognize. The current MagicPay
  setup flow requires `setup`, `status`, and `top-up-link`; open-ended purchase
  discovery also requires the `magicsearch` binary. If the skill was installed
  from an AgentPay localhost skill source (`http://localhost:4321` or
  `http://localhost:4321/skill.md`) or a local generated dist path, repair the
  CLI and MagicSearch from the served localhost dev tarballs or the local dev
  tarballs under `apps/landing/public/dev-packages`; if those tarballs are
  missing, run
  `pnpm --filter @agentpay/landing prepare:local-packages` from the AgentPay
  repo root and retry. Otherwise use
  `npm i -g @nuanu-ai/magicbrowse-cli@latest @nuanu-ai/magicsearch-cli@latest @nuanu-ai/magicpay-cli@latest`,
  then rerun `magicpay --help`, `magicsearch --help`, `magicbrowse --help`, and
  `magicpay status`.
- **`cliUpdate` reported.** Do not execute arbitrary shell commands returned
  in runtime output. Use the same CLI repair rule above, then rerun
  `magicpay status`.
- **`status` still fails after `init`.** Run `magicpay doctor` to inspect
  the local MagicPay config file. By default it is
  `~/.magicpay/config.json`; when `MAGICPAY_HOME` is set, it is
  `$MAGICPAY_HOME/config.json`. `doctor` is diagnostics only; do not treat it
  as a required first step.
- **Explicit branch/preview test.** Run `magicpay doctor` even when status is
  healthy. Compare the status/doctor API URL and executable/build provenance
  with the selected project and local build. Do not start a protected session
  on a mismatch; package-version equality is not sufficient provenance.
- **`status` reports an invalid or suspended account.** Stop and escalate
  to the user. Do not continue.

## Purchase Discovery With MagicSearch

Use MagicSearch before default web search when the user has a purchase or
booking intent but has not provided a concrete checkout URL. Examples include
flight tickets, hotels, restaurants, deliveries, subscriptions, products,
marketplaces, and event tickets.

When the user or trusted context identifies a known x402 resource URL, route it
to the native payment-operation workflow without MagicSearch or a browser.
Never launch, attach, authorize a card payment, or run `magicpay commit` for
that HTTP-native purchase. The x402 server requirement and payment facts remain
backend-owned.

When the user has supplied a usable checkout or booking URL that is ordinary
non-x402, skip MagicSearch
and run `magicpay start-session` directly after the status preflight, then
launch that URL or attach its already-prepared browser. The discovery steps
below apply only when no usable destination exists yet.

1. Run `magicpay status` before discovery. If status is missing or unhealthy,
   recover setup first.
2. Build a refined purchase prompt from user-provided facts only. Extract
   structured slots first: dates, origin, destination, one-way or return,
   party size, product names, merchant preferences, country, region, place,
   baggage, cabin, and currency when the user supplied them. For travel, verify
   direction before search; never send a prompt that can reverse origin and
   destination.
3. Run MagicSearch with automatic provider routing. Provider selection is an
   implementation detail; do not ask the user to choose between providers, MCP
   tool profiles, or entries such as Google Flights versus Apify.
   This step owns the provider-index lookup and Exa/search fallback. Do not
   launch MagicBrowse, ordinary web search, or another browser fallback until
   MagicSearch has either returned a target or failed/blocked explicitly.

   ```bash
   magicsearch query "<refined purchase prompt>" --choice-policy never --json
   ```

   Keep currency inside the refined prompt and never add `--currency` to
   `magicsearch query`; that option belongs to provider discovery, not query.

   Add useful hints when known:

   ```bash
   magicsearch query "<refined purchase prompt>" --category flights --country ID --choice-policy never --json
   ```

   If `magicsearch query` returns `choice_required` for actual purchase
   options, resolve the user's choice and obtain the selected URL before
   `magicpay start-session`. Do not start the protected product session merely
   to host a query choice. The provider-execution flow below is different:
   `magicsearch discover` may require an active session for its tokenized
   choice.

4. If MagicSearch selects a supported MCP discovery provider, run provider
   execution before browser handoff. For Google Flights/Fli, extract IATA
   route/date slots from the user facts and run:

   ```bash
   magicpay start-session "<short task name>"
   magicsearch discover "<refined purchase prompt>" --category flights --origin DPS --destination SIN --departure-date 2026-07-12 --json
   ```

   One live MagicPay session resolves automatically. With several parallel
   sessions, pass the id from `magicpay start-session` explicitly — export
   `MAGICPAY_SESSION=<sessionId>` or add `--session <sessionId>` to each
   `magicsearch` command.

   Use server-side MagicSearch choice only when the choices are actual
   user-facing purchase options, such as itineraries, hotels, rooms, seats,
   tickets, plans, or comparable checkout offers. Do not use
   `choose-target --choice-policy always` to create travel choices; that
   command can expose provider/search-target choices before provider
   execution.

   When the result is `status: "choice_required"`, present the choice both
   ways: give the `requestUrl` link to the user AND duplicate the returned
   `options` in chat as a numbered list with each option's important details
   (title, subtitle, price, duration/stops or comparable characteristics), so
   the user can reply with a number here or pick in the link. Then immediately
   run the returned `pollCommand` or the equivalent command below and wait for
   the selected URL. Do not stop after sharing the link and do not ask the
   user to come back to chat after choosing in the UI. If the user replies
   with a number, submit `options[n-1].id` via
   `magicsearch choose --request <requestId> --choice <choiceId> --json`
   instead of continuing to poll:

   ```bash
   magicsearch choose --request <requestId> --json
   ```

   That command follows the canonical request loop until the user completes
   the tokenized request or a typed safety bound requires one reconciliation.

   If you display the safe `options` titles/prices/URLs in chat and the user
   chooses in chat instead of the UI, submit the exact backend-owned id:

   ```bash
   magicsearch choose --request <requestId> --choice <choiceId> --json
   ```

   Use the selected URL from that result as the starting target.

5. If `magicsearch query` returns `provider.methodType: "mcp"` and
   `execution.mcp.profile: "fli"`, do not open the generic Google Flights URL
   yet; run `magicsearch discover` with the extracted flight slots. Use a
   browser handoff only after provider execution returns a concrete
   booking/search URL, or when MagicSearch used Exa/search fallback because no
   provider URL was available. A result with `source: "exa"` or
   `searchProvider: "exa"` is a successful MagicSearch target and should be
   used before MagicBrowse page-control fallback. If no product workflow
   session is active yet, continue with `magicpay start-session` and browser
   launch or attach before Memory fill, approval, or final checkout actions.
6. If MagicSearch returns `choice_required` for a provider/tool-profile choice,
   do not show it to the user; rerun with `--choice-policy never`. If it returns
   multiple actual purchase options without a server-side request, or missing
   required details, ask the user for the choice or missing fact, then rerun the
   provider execution command with the refined prompt and structured slots.
7. If MagicSearch is unavailable, blocked, or returns no usable target, state
   that fallback explicitly before using ordinary web search. Do not silently
   skip MagicSearch.

For travel discovery, MagicSearch may select an MCP-backed provider method such
as a hosted flight-search tool. Do not bypass that method with generic web
search while it is available. If the tool returns multiple viable itineraries,
hotels, rooms, or tickets, use MagicSearch/MagicPay choice and wait for the
user selection before calling deeper booking-detail or checkout-resolution
tools for the selected option.

MagicSearch selects a provider, checkout target, or discovery URL. It does not
approve payment, reveal Memory values, or authorize final browser actions.
Keep all checkout, Memory fill, typed approval, and final submission rules from
this guide.

## Start From The Product Session

- After preflight, run `magicpay start-session [name]` before any normal
  MagicPay browser launch or attach.
- For isolated test or parallel workflows, set a distinct `MAGICPAY_HOME`
  before running MagicPay commands. This isolates MagicPay config, workflow
  state, browser-session pointer, and run files. Browser-runtime diagnostics
  remain separate and still use `MAGICBROWSE_HOME` when that layer is involved.
- Use `magicpay launch [url]` when MagicPay should create the browser child
  inside the active product workflow.
- `magicpay launch` returns the child's `cdpUrl`. Pass it to a
  page-control tool (for example `magicbrowse attach <cdpUrl>`) when
  that tool should drive the same browser inside the workflow. This is an
  in-workflow bind of an owned disposable browser, not an external attach
  that needs separate user approval; still keep the endpoint private.
- If another tool or the user already has the correct page open, use
`magicpay attach <cdp-url>` only for that approved private browser process.
  A page prepared in a browser without a reachable CDP endpoint cannot be
  adopted; the flow must be redone in an attachable or MagicPay-launched
  browser.
- If the CDP endpoint changes, rerun `magicpay attach` before retrying
  browser-dependent commands.
- If MagicPay is already bound to the same approved endpoint inside the active
  workflow, repeating `attach` is allowed but not required as a setup ritual.
- Do not carry one browser child binding across different product workflow
  sessions. Keep CDP endpoints private.
- MagicPay does not own browser teardown. `magicpay close` closes or clears the
  browser child while leaving the product workflow active. `magicpay
end-session` completes the MagicPay workflow.

## CAPTCHA Recovery

- If a CAPTCHA is already visibly confirmed on the bound page, run
  `magicpay solve-captcha [--timeout <s>]` directly; do not call
  `magicpay commit` to confirm it.
- Only call `magicpay solve-captcha [--timeout <s>]` when a real CAPTCHA is
  confirmed present on the current page.
- `solve-captcha` uses the current browser child inside the active MagicPay
  product workflow. It does not close the browser or create a new one.
- When solver verification and structural detection disagree, the command
  performs at most one rendered-state read of the CAPTCHA region. Follow the
  returned `agentInstructions`; visual evidence never authorizes Pay, commit,
  or a retry.
- Continue only when the solver reports `fullyResolved: true`,
  `merchantCleared: true`, and `outcomeType: "resolved"`. `solverVerified`
  alone is not merchant clearance. A result with `success: true` but
  `fullyResolved: false` or `outcomeType: "partial"` is not clearance: do not
  mark the CAPTCHA resolved or commit. Surface the unresolved challenge. When
  the challenge followed a dispatched final click, keep following the exact
  returned `payment-result` reconciliation; CAPTCHA state does not establish
  whether a provider attempt exists.
- After a fully resolved solve, get fresh visible page state from the current
  page-control owner. Do not invent or run a page-state CLI such as
  `magicbrowse get-page-state`; that command is not documented. Obtain fresh
  visible state only through the existing page-control owner's documented
  continuation. If an old checkout plan is involved, rerun `magicpay plan-fill`
  and execute its exact returned `applyCommand` before resuming. No `magicpay
  observe` command is documented in this bundle. CAPTCHA clearance alone does
  not authorize `magicpay commit`; commit only at the normal matching-approval
  and current-live-facts boundary.
- A fully resolved solve after a final click does not authorize another commit.
  Require a provider-terminal result for the prior attempt and a fresh payment
  authorization before another final click.
- When continuation is owned by MagicBrowse, run
  `magicbrowse mark-captcha-resolved` only after a fully resolved solve and
  before the next `magicbrowse act`.
- When a user manually completes a post-click challenge, run
  `magicbrowse mark-captcha-resolved` and make `magicpay payment-result` the
  next observer before any `magicbrowse act`, so the same uncertainty latch
  records the trusted clearance.

## Fill Recovery Ladder

Use one default path. The escape hatch is only for a visible field that the
default missed or targeted incorrectly; it is not an alternative fill system.

**Default:** plan and apply from the live page.

- If raw text, checked/selected state, and the final action appear to disagree
  about recurrence, run `plan-fill` before asking the user. It stabilizes the
  targets and uses one visual read only when structured evidence remains
  ambiguous. Ask only when the hybrid result is still unclear.

- Run `magicpay plan-fill` on the current
   bound browser page. Use `--planner-hint <text>` only for short context
   about the form. Never pass raw values, target matches, target lists, Memory
   catalogs, materializers, or browser writers.
   If the result includes `nextAction: "apply-fill"` or
   `memoryRequestHandoff.status: "requires_apply_fill"`, do not stop or tell
   the user that no secure request link was generated. `plan-fill` is
   value-free and does not create hosted links; run exactly the returned
   `applyCommand` first so MagicPay can either fill approved Memory or create a tokenized
   missing-data `requestUrl`.
- Run exactly the `applyCommand` returned by `plan-fill`. Request links always
   open on the production web app (swap the domain by hand for local testing);
   use `--hosted-base-url` only for an explicit one-command diagnostic override. It materializes
   approved values internally, fills only planned fields, and stops before any
   final commitment control. If `apply-fill` returns a candidate-choice
   blocker without a `requestUrl`, show only the safe labels and continue with
   `magicpay choose-memory --choice <choiceId>`.
   If `apply-fill` returns `status: "waiting_for_user"`, follow its structured
   action. For `chat_question`, ask the exact grouped question and send the
   user's reply only through stdin to the returned `replyCommand`. For
   `memory_confirmation`, run the returned allow or deny command after the
   user's answer. For `memory_choice`, show only safe labels and run the command
   attached to the selected choice. For `hosted_request`, share `requestUrl`,
   immediately run its `pollCommand`, and then its `resumeCommand` when ready.
   Login credentials keep the protected relay and payment-card data keeps the
   provider-delegated executor: never ask for those in chat and never ask the
   user to type sensitive data directly into the merchant form. Never place a
   raw chat reply in argv or build a value-bearing decision JSON yourself.
- If page evidence changed, the browser
   binding became stale, a target disappeared, or `apply-fill` reports
   `target_not_found` / `stale_target`, refresh or re-observe the page and
   return to `plan-fill`. Do not reuse the old plan.

**Bounded escape hatch:** use `fill-field` only for targeting recovery.

- If `plan-fill` /
   `apply-fill` missed a visible field or chose the wrong observed target, and
   the agent can identify the correct Memory item/field plus the current
   observed target id, run:

   ```bash
   magicpay fill-field --field-ref field.email --target 1 --item-ref mem_profile
   ```

   `fill-field` accepts one value-free assignment per invocation: `fieldRef`,
   `target`, optional `itemRef` or `itemId`, and optional `projectionPart`.
   `--target` accepts the bare observed id such as `1` or the canonical
   `selector:1` ref. It fetches the current Memory catalog, resolves backend
   handles, refreshes target state, validates approvals/provider state/target
   writability/projection, and writes through the same browser bridge as
   `apply-fill`. It returns the same apply-style result shape: `status`,
   `fields`, `fieldDiagnostics`, and `completedLedger`.

- Stop or ask instead of guessing. `fill-field` is not a fallback for
   `matcher_unavailable`, missing browser connection, auth/CAPTCHA walls,
   missing Memory, denied approval, unsupported targets, or raw-value entry.
   For those states, follow the status guidance: rebind, replan, ask the user,
   use typed approval, or stop.

Use `projectionPart` only for a visibly split typed value target. Supported
parts are `year`, `month`, `day`, `country_code`, `national_number`, `given`,
`family`, `segment_1`, `segment_2`, `segment_3`, and `segment_4`.
Projection diagnostics mean the part or target shape is unsafe; refine only
from visible evidence, otherwise ask, skip optional fields, or stop.

## Memory Fill Recovery

- `start-session` attempts to cancel/clear a stale previous workflow binding
  before it creates the new product session. If that recovery is still
  blocked, start manual recovery with `magicpay status`, then either
  `magicpay end-session` or a fresh `start-session`.

- Run `magicpay plan-fill` on the current page before applying saved Memory.
  Use `--planner-hint <text>` only for short human-readable context; do not
  pass raw values, target matches, catalogs, materializers, browser writers, or
  page target lists.
- If `plan-fill` reports `matcher_unavailable`, fail closed or retry only after
  the gateway/tooling state changes. Do not fall back to deterministic matching.
- If `plan-fill` reports a non-blocking blocker
  `payment_card.authorization_required`, the backend is saying that a
provider-backed payment card exists but this active MagicPay session
  is not authorized to reveal card handles yet. This is not a matcher failure
  and not a reason to ask for PAN/CVV. The advisory alone does not trigger an
  authorization: require protected card fields in the current plan. If this is
  an outer support/donation control, guarded-commit it to open the payment form,
  then re-plan and authorize against that form. If the task needs those card fields, collect the
  visible payment authorization facts and keep missing live facts unknown. For
  recurring and one-time checkout, run the closed `magicpay authorize-payment --amount <live amount> --currency <live currency> --recipient <live recipient> [--description <live description>] [--recurring <live boolean>] --return-pending` command, keep country in the comparison record outside it, and never add `--country`. For recurring checkout, authorize from this plan so the same typed request binds the payment facts and observed subscription terms. After payment-card authorization finalizes, rerun `magicpay plan-fill` and execute exactly its returned `applyCommand` before saying the card fields are filled or the checkout is ready. Never write, show, or execute a hand-written or sample `magicpay apply-fill`, `magicpay wait-request`, or `magicpay wait-memory`; use only exact returned command fields.
- If `plan-fill` reports `taskControls`, those are page controls that configure
  what is being bought — a quantity, a tier, a billing period — not data to
  fill. Never relay one to the user and never write a value into one: set it by
  clicking the option the approved task calls for, then rerun `plan-fill`.
  Read the option from the page, not from the label alone — a donation page
  labels its options `1`, `3`, `5` for coffee counts, so an approved $5 is the
  option `1`, not the option `5`. Each entry carries `selected: true` when the
  page already has that option chosen; if the currently selected option is the
  one the task calls for, leave it alone. If nothing on the page tells you which
  option the task means, stop and ask rather than accepting the default —
  the default decides what gets bought.
- If the page changed after planning, rerun `plan-fill` instead of applying a
  stale plan.
- Run exactly the `applyCommand` returned by `plan-fill` for the active plan. Generated request form links
  always open on the production web app; for local admin testing swap the
  domain by hand, or use `--hosted-base-url` only as an explicit one-command
  diagnostic override. It
  fills planned fields only and does not submit the page.
- Payment-card availability never enters the Memory request flow. A stale or
  missing session authorization becomes the typed `authorize-payment` next
  action. A configuration, catalog, storage, or provider execution failure
  becomes `payment_method_unavailable` and is a hard stop. Never tell the user
  to connect or reconnect a provider, and never run `wait-memory` for
  `provider_needs_reauth` or `provider_unavailable`.
- If `apply-fill` returns `status: "waiting_for_user"` with a
  `memory.provide_missing`, `memory.choose_candidate`, or
  `memory.ask_before_use` blocker, follow the structured action returned by
  MagicPay. Do not infer the account's `memorySource` preference yourself.
  - `chat_question`: ask the exact grouped `question`, then pass the user's raw
    reply only through stdin to the exact `replyCommand`. Never place the reply
    or mapped values in argv, logs, summaries, or a hand-written decision JSON.
    The command submits `save:false` and resumes through the canonical request.
  - `memory_confirmation`: ask the exact question and run the exact returned
    `allowCommand` or `denyCommand`. Every existing ordinary item still needs
    this confirmation in chat mode.
  - `memory_choice`: show only each `safeLabel`, then run the exact command for
    the selected choice. Selection also confirms that exact item revision.
  - `hosted_request`: share `requestUrl`, run the exact `pollCommand`, then run
    the returned `resumeCommand` when ready.
  A hosted result with `memoryReady: true` authorizes its exact
  `resumeCommand`; an ordinary chat result asks one grouped chat question and
  sends the reply only through its exact stdin command.
- The chat path applies to general values only. **Login credentials keep the
  protected relay** (`memory.resolve_form` with its `requestUrl`; values are
  `secret`/handles-only and never appear in chat), and **payment-card data
  keeps the provider-delegated executor** — never ask for either in chat and
  never ask the user to type them into the merchant form directly. Do not use
  `magicpay wait-request` for Memory request links.
- If a login or card blocker has no `requestUrl`, stop and report that the
  secure request link could not be generated; those flows have no chat
  fallback.
- Never change `memorySource` on the user's behalf. The session's pinned policy
  determines which structured action appears; account Settings affect only new
  sessions.
- Continue after a successful fill with the page-control owner, but first refresh
  the visible page state.
- If required fields remain empty after Memory fill, ask the user how to
  proceed or stop. Do not invent values and do not fill directly from chat
  text.
- For `apply-fill.fieldDiagnostics`, treat diagnostics as facts. The agent
  chooses remediation from the result-state policy table; in particular,
  `target_not_writable` is not a blind replan signal.
- If `plan-fill` / `apply-fill` missed a visible field or matched the wrong
  target, and you can identify the correct Memory item/field plus observed
  target id, use `magicpay fill-field --field-ref <fieldRef> --target <target>`
  as a lower-automation recovery step. Do not use it as the default path, and
  never pass raw values.
- Before any consequential browser action, get the matching typed MagicPay
  approval for the current site/merchant, exact action, and visible amount or
  data.
- For protected action approval handoff, always add `--return-pending` to the
  typed action command: `authorize-payment`, `sign-message`, or
  `confirm-action`. Without it the command blocks for the full request lifetime
  and the user is never handed a link to act on.
  The active MagicPay profile supplies the local or hosted-development origin.
  Give the user the returned tokenized `requestUrl`, then immediately run the
  exact returned `pollCommand`. Do not
  ask the user to tell you after they approve; polling observes the same
  decision whether it comes from the link, admin, mobile app, or another
  MagicPay UI. For `authorize-payment`, tell the user they can approve in
  MagicPay UI with the link or send the one-time code from the MagicPay email.
  If they provide OTP, run the exact returned `confirmOtpCommand`, then continue
  the exact returned `pollCommand`. For `sign-message` and `confirm-action`, use the
  link only; do not ask for OTP.
- If `apply-fill` or a typed action command returns terminal `denied`,
  `expired`, `failed`, or `canceled`, stop the MagicPay path and report the
  exact state. A diagnostic timeout, caller abort, or request safety bound is
  non-terminal: preserve request identity and run the exact returned
  `pollCommand`.
- After typed approval, proceed with exactly that action; stop only if page
  facts changed.
- After submitting a form, always observe the resulting page before claiming
  success or progress. If navigation or a clear confirmation page appeared,
  continue from that state and run `magicpay payment-result`. Share returned
  recovery copy and links exactly, keep pending/unknown results open, and run
  the exact returned `recovery.pollCommand`. Do not infer provider settlement from the
  merchant page. If the browser is still on the form with validation messages
  or invalid fields, follow the post-submit result policy; do not retry
  blindly.

## What MagicPay Stores

MagicPay Memory holds saved items and field descriptors. The public fill path
uses value-free descriptors and opaque refs during planning, then materializes
only the approved values needed by the active plan during apply.

Treat a Memory item as a user-owned reusable data record, not as a single field.
The item label is the human-readable name for that record and should describe
the group of fields that future fills may choose together. Good labels name the
purpose: `Airline login`, `Traveler profile`, `Home shipping address`, `Wallet`,
or `Facts about user`. Do not put raw values in the label, do not use one field
name as the item label when the item contains a broader record, and do not create
one item per field unless the user is saving one truly standalone fact.

Use `Facts about user` only for global profile facts with no narrower record.
Use narrower labels for site/account-specific logins, traveler profiles,
addresses, wallets, payment-related records, and other coherent groups. When
chat-provided reusable facts need saving, list Memory items first, update the
semantically suitable editable item, and create a new item only when no suitable
record exists.

The user's MagicPay Memory holds reusable items with human field labels,
human-readable hints, opaque `fieldRef` identifiers, and optional public value
types. Use labels such as `Login email`, `Password`, `Full name`, `Date of
birth`, or `Phone` for user-facing text and matcher evidence; use `fieldRef`
for existing-field identity in update/apply flows. Hints explain when a field is
useful without containing raw values.

Public editable value types are only:

- `date` — canonical value `YYYY-MM-DD`;
- `phone_number` — canonical E.164 value, for example `+14155550100`;
- `person_name` — non-empty full name string.

When no value type is present, Memory fill treats the field as ordinary direct
fill and does not split or normalize it. Internal card value types such as
`payment_card_number` and `payment_card_expiry` belong only to provider-backed
payment-card Memory surfaced by MagicPay after authorization; do not set or
request those types through public Memory CRUD.

Do not assume emptiness or abundance from prior context. If you need to know
whether saved Memory can fill the current page, run `magicpay plan-fill` and
branch on its result. If you need to list Memory items manually, pass the
current page URL with `magicpay list-memory-items --url <current-url>`; use
`--all-sites` only for explicit global Memory review or editing. Do not read or
print raw Memory contents yourself.

For Memory CRUD, list first and use stable refs. Create a new item with
`magicpay create-memory-item --item-label <label>` plus field shortcuts such as
`--text "Login email=ada@example.com"`, `--date "Date of birth=1815-12-10"`,
`--phone "Phone=+14155550100"`, or `--person "Full name=Ada Lovelace"`.
Use `--secret-text`, `--secret-date`, `--secret-phone`, or `--secret-person`
when the new field should be hidden in display/logging. For existing fields,
never address by label: use `magicpay update-memory-field --field-ref
<fieldRef>` or `magicpay delete-memory-field --field-ref <fieldRef>`. Use
`magicpay add-memory-field --item-id <itemId> --label <label> --value <value>`
to add one field to an existing item. `--secret true|false` is mutable
display/logging metadata for any field, not encryption. Use raw JSON only when
the user explicitly asks for a service/debug payload.
During an active fill, do not use the direct update command to correct a value
the merchant rejected. Run `magicpay correct-memory-field --field-ref
<fieldRef>` instead. It creates one secure hosted request that updates the
exact field and grants the resulting item revision for the current host and
session. Run exactly its returned `pollCommand`; when it reports
`memoryReady: true`, run exactly the returned `resumeCommand`. Never put the
replacement value on the CLI command line or treat a chat correction as the
backend decision.

<!-- magicpay-continuation:v1 id=workflow-memory-correction action=poll-before-resume -->
Run exactly the returned `pollCommand` before exactly the returned `resumeCommand`.
<!-- /magicpay-continuation:v1 -->
An ordinary `chat_question` may use one grouped chat question, but its raw
reply still goes only through stdin to the exact returned `replyCommand`.
Provider-backed payment cards are special: before payment authorization,
`plan-fill` can show that a card exists through an
`authorization_required` Memory availability entry, but it does not expose
card field handles. Card handles appear only inside the active MagicPay
session after the matching payment authorization is approved.

## Payment Authorization Facts

Before `magicpay authorize-payment`, collect the visible transaction facts
from the current checkout/review page and the user's task:

Immediately before creating the payment approval, run `magicpay
payment-balance` without asset flags and verify that unified available balance
covers the maximum debit. Tell the user, in the language they are using, that
the unified balance was checked and include the available and required amounts.
If it is insufficient, do not create the approval. The backend atomically
rechecks and reserves that unified balance after approval and before provider
submission.

Never invent or use placeholder/fallback `amount`, `currency`, `recipient`,
`recurring`, or `country` values before the live selected target and checkout
supply those facts. A budget ceiling, catalog or search-result price,
product-country guess, and literal `MerchantName` are placeholder/fallback
values, not payment authorization facts. Stop or ask when a required fact is
not yet live and unambiguous.

For a normal live checkout, run the closed `magicpay authorize-payment --amount <live amount> --currency <live currency> --recipient <live recipient> [--description <live description>] [--recurring <live boolean>] --return-pending` command. Keep `country: <live country>` in the comparison record outside the command, never add `--country`, and keep every missing live fact unknown.

- `amount`: the final amount the user is about to authorize, including visible
  taxes, fees, discounts, or subscription-period pricing. Do not use subtotal
  when a final total is visible.
- `currency`: an explicit three-letter code such as `USD` or `EUR`. A symbol
  alone is not enough unless page or user context makes the code clear.
- `recipient`: the merchant or payee the user believes they are paying.
- `country`: the visible checkout or billing country used by the live form.
  It must agree with the user's task and remain unchanged through commit.
- `description`: optional short product, plan, order reference, subscription,
  donation, or purpose summary.
- `recurring`: optional boolean. Set it only when the page or user task is
  clear; ask the user if recurring status materially affects approval and is
  unclear.

For a recurring checkout, plan the live form before `magicpay authorize-payment`.
The current plan supplies the observed subscription terms, allowing one typed
request to authorize both those terms and the matching payment. If the command
returns `reason: "plan_fill_required"`, run `magicpay plan-fill` and retry the
authorization once. Do not create a separate subscription approval for the
same unchanged checkout.

Merchant/payee sourcing rules:

- Prefer the merchant name from the checkout header, order summary, invoice,
  payment confirmation text, or the user's task.
- Do not use payment processor or card-provider names such as Stripe,
  Checkout.com, Mercuryo, Apple Pay, Google Pay, Visa, or Mastercard as
  `recipient` unless that provider is the actual merchant.
- Treat page title, hostname, and URL as supporting signals only. Use them as
  the merchant name only when they clearly identify the payee and no stronger
  visible label is present.
- Normalize obvious checkout boilerplate, but keep meaningful brand or legal
  qualifiers that are part of the visible merchant name.

Escalate to the user when:

- final amount is not visible, conflicts across the page, or could be subtotal
  instead of total;
- currency is missing or ambiguous;
- merchant/payee cannot be distinguished from the payment processor;
- recurring status matters and cannot be determined from visible context;
- country is missing, conflicts with the task or live form, or changes after approval;
- visible checkout facts conflict with the user's stated task.

Do not change existing `itemRef` behavior while collecting payment facts.
`itemRef` remains a Memory item selector outside action params. Do not type,
print, or pass card PAN, CVV, wallet private keys, passwords, or other
protected values through the agent prompt or action params.

After successful `authorize-payment`, continue with that exact payment:
protected payment artifact use, payment form fill, and final Pay/Submit are
covered while `amount`, `currency`, `recipient`, `recurring`, and country stay
unchanged. Stop and ask again if any of those facts change.

### Recovery Sequence For Changed Fill Plans

When the page changes after planning, the stored Memory plan may no longer
match the live DOM. Do not retry with the same stale plan.

1. Let the page settle — wait for any in-flight re-render to finish.
2. Run `magicpay plan-fill` on the current page.
3. If planning cannot produce safe matches, ask the user or re-navigate; do
   not guess.
4. If planning succeeds, run exactly the returned `applyCommand`.
5. Do not reuse a plan from before step 2.

## Multiple Sensitive Fields

When one form needs several saved Memory fields:

1. Run one `magicpay plan-fill` for the current page.
2. Run exactly the `applyCommand` returned by `plan-fill` for the active
   `apply-fill` plan.
3. Refresh the current page state after fill if the page mutates.
4. Continue with the page-control owner after the required visible fields are
   complete.
5. Get the matching typed MagicPay approval if the next browser action would
   submit, purchase, log in, save account settings, or otherwise commit state.

## After `end-session`

`magicpay end-session` marks the MagicPay workflow complete and keeps the
browser available. After it returns, hand control back to the caller-owned
browser lifecycle:

- if another tool launched an owned disposable browser only for this task,
  that tool may close its own session after the user no longer needs the page;
- if the browser was an existing/user-owned session, an approved CDP attach,
  a named profile, or a page the user wants to inspect, leave it open unless
  the user explicitly approves teardown.

Do not encode a MagicBrowse dependency into MagicPay orchestration. The same
rule applies to any browser lifecycle owner: MagicPay ends the protected
workflow; that owner decides cleanup.

## When To Stop

Stop and report back when:

- request resolution reaches a terminal denied, expired, failed, canceled, or
  timeout state;
- OTP is invalid, expired, or exhausted and the request cannot continue through
  another supported approval path;
- the browser is no longer on the intended sensitive page;
- Memory planning stays ambiguous or unavailable after rerunning it on the
  current page;
- the next step would submit or run a sensitive action and there is no
  matching typed approval for the unchanged current site/merchant, action, and
  visible amount or data;
- `magicpay status` still fails after `magicpay init <apiKey>` and
  `magicpay doctor` confirms a local config problem that needs repair;
- `magicpay status` says the account or API key is invalid.
