# MagicPay Boundaries

<!-- magicpay-continuation-contract:v1 -->
## Contents

- [What This Skill Owns](#what-this-skill-owns)
- [Consequential Action Approval](#consequential-action-approval)
- [Readiness Rules](#readiness-rules)
- [Browser Authority](#browser-authority)
- [CAPTCHA Recovery](#captcha-recovery)
- [Memory Fill Rules](#memory-fill-rules)
- [Protected-Action Rules](#protected-action-rules)
- [Secrecy And Safety](#secrecy-and-safety)
- [Ask The User When](#ask-the-user-when)
- [Trust Model And Command Narration](#trust-model-and-command-narration)
- [Rare And Failure Guardrails](#rare-and-failure-guardrails)

## What This Skill Owns

- Start or continue the MagicPay product session.
- Launch or attach an approved browser as a child resource inside that active
  session.
- Plan Memory field fill with `magicpay plan-fill`.
- Apply approved Memory values with `magicpay apply-fill` without submitting.
- Return post-fill page continuation to the page-control owner.
- Run typed protected action approvals through `authorize-payment`,
  `sign-message`, or `confirm-action`.
- Complete the MagicPay workflow with `magicpay end-session`, then return
  browser lifecycle decisions to the caller-owned browser tool or
  orchestrator. `magicpay close` closes or clears only the browser child.
- Recover from a confirmed real CAPTCHA on the current browser child with
  `solve-captcha`. Only when it reports `fullyResolved: true`,
  `merchantCleared: true`, and `outcomeType: "resolved"` may you call
  `magicbrowse mark-captcha-resolved`
  before continuing through MagicBrowse when MagicBrowse owns the next step.

## Consequential Action Approval

All server-side user requests use the matrix and One User-Request Loop in
`SKILL.md`. Share the secure link and immediately run the exact returned
`pollCommand`. Keep the same process and request id through pending states,
output loss, or caller interruption; recover once with `magicpay requests` and
never create a replacement merely because polling stopped. Request safety
bounds require one reconciliation and a report when still overdue.

Before any submit, protected action, purchase, login, identity submission,
account change, or other consequential action, get the matching typed
MagicPay approval for:

- the current site or merchant;
- the exact action to be taken;
- the visible amount, country, account, identity, or other data being submitted;
- whether the user wants final submission now.

MagicPay fills planned fields only. After `magicpay apply-fill`, continue with
the page-control owner from a refreshed page state. Do not treat filled fields as
approval to submit.

After typed approval, proceed with exactly that action; do not ask for a
second approval unless approved page facts changed. `authorize-payment` covers
the matching payment artifact use, payment form fill, and final Pay/Submit
while `amount`, `currency`, `recipient`, `recurring`, and country stay unchanged.
`sign-message` covers the exact message only. `confirm-action` covers only the
summarized non-payment consequential action.

After any approved submit, observe the resulting page before claiming success,
progress, or failure. If the page is still on the same form with validation
errors, classify the visible result before choosing a recovery path. Do not
infer or reveal hidden Memory values from the error text.

A merchant's own button often does not charge anything. "Support $5", "Donate"
and "Checkout" frequently hand off to a payment provider, so the click that
looks like the commitment only opens the card form. `magicpay commit` detects
this and returns `commitment_opened_payment_form` with
`nextAction: replan_and_fill_payment_form`: an empty card field appeared where
the result should be, so **nothing has been charged**. Run `magicpay plan-fill`
against the new form, run exactly its returned `applyCommand`, then
`magicpay commit` its own
submit control. Do not run `payment-result` — there is no transaction to report
and it will stay pending forever.

After a payment submit, run `magicpay payment-result`. Provider-backed success
is the only basis for reporting settled payment. Keep pending and unknown
results open. For recoverable failure, share the returned user message and
tokenized links, run the exact returned `recovery.pollCommand`, and require a
fresh payment authorization for any retry. Never retry or top up automatically.

## Readiness Rules

- Use `magicpay status` before a new MagicPay Memory fill task.
- If `status` reports a missing or invalid API key, run `magicpay init`.
- If the installed CLI lacks a command required by this skill, run
  `magicpay --help` and repair the CLI before continuing. For local AgentPay
  skill installs, prefer the local dev tarballs under
  `apps/landing/public/dev-packages`; otherwise use
  `npm i -g @nuanu-ai/magicbrowse-cli@latest @nuanu-ai/magicsearch-cli@latest @nuanu-ai/magicpay-cli@latest`.
- If `status` reports `cliUpdate`, use the same CLI repair rule, then rerun
  `status`.
- Use `doctor` only when local config still looks broken after `init`.
- Normal product work starts with `magicpay start-session` before
  `magicpay launch` or `magicpay attach`.

Do not print, log, or share `MAGICPAY_API_KEY`, the local MagicPay config
file, or CDP endpoints. The config file is `~/.magicpay/config.json` by
default or `$MAGICPAY_HOME/config.json` when `MAGICPAY_HOME` is set. Memory
item ids are operational refs: pass them only between MagicPay commands that
require them, and never show them to the user or put them in reports/external
logs. If the environment is shared or compromised, stop and ask the user to
revoke or rotate the key.

## Browser Authority

Use `magicpay launch` or `magicpay attach` only inside an active product
session. Use `attach` only for the private browser process the user
approved for this task. A CDP endpoint inherits the authority of any logged-in
browser state. Keep endpoints private and do not paste them into shared logs.
Run `attach` when MagicPay is not yet bound to the approved browser child, or
when the CDP endpoint changed. Re-attaching the same endpoint is allowed but
is not required as a ritual.

Browser teardown remains outside MagicPay's product-session authority.
`magicpay close` closes or clears the browser child while keeping the product
workflow active. If the browser was launched as an owned disposable session by
another tool, that tool can clean up after the overall task is done. If the
browser was external, user-owned, or handed to the user for inspection, leave
it open unless the user explicitly approves teardown.

## CAPTCHA Recovery

Only call `magicpay solve-captcha [--timeout <s>]` when a real CAPTCHA is
confirmed present on the current browser child inside the active product
workflow. Do not use it as page waiting, challenge detection, or a generic
retry.

When a CAPTCHA is already visibly confirmed, run
`magicpay solve-captcha [--timeout <s>]` directly; do not call
`magicpay commit` merely to confirm the challenge.

`magicpay commit` returning `commitment_blocked_by_challenge` is such a
confirmation: it read the page back after the click and found a verification
wall standing where the result should be. Because the final click was already
dispatched, first run the exact returned `payment-result` command. The wall does
not prove whether the merchant contacted the provider. Do not commit again
while that attempt is submission-uncertain.

Only `fullyResolved: true` with `merchantCleared: true` and `outcomeType:
"resolved"` means the challenge is cleared. `solverVerified` alone is not
merchant acceptance. A result with `success: true` but `fullyResolved: false` or
`outcomeType: "partial"` is not clearance: do not mark the CAPTCHA resolved,
or commit. Surface the unresolved challenge while continuing any provider
reconciliation already required by the final click. Solver clearance alone
never authorizes another final click.

If a partial result includes `renderedStateAssessment`, follow the returned
`agentInstructions`. A bounded visual read can distinguish a visibly active
challenge from a likely cleared one, but it cannot authorize Pay, commit, or a
retry.

After full resolution, get fresh visible page state from the current page-control
owner. Do not invent or run a page-state CLI such as `magicbrowse get-page-state`;
that command is not documented. Obtain fresh visible state only through the
existing page-control owner's documented continuation. No `magicpay observe`
command is documented in this bundle. If an old checkout plan is involved,
rerun `magicpay plan-fill` and execute its exact returned `applyCommand` before
resuming the documented current flow. CAPTCHA clearance alone does not authorize
`magicpay commit`; commit only at the normal matching-approval and
current-live-facts boundary.

When the next step is owned by MagicBrowse and the solve fully resolved, call
`magicbrowse mark-captcha-resolved`, then continue with
`magicbrowse act "continue..."`. The marker only tells MagicBrowse that an
external participant resolved CAPTCHA for this page; MagicBrowse still checks
the actual page state and must stop again if CAPTCHA or human verification is
still visible.

## Memory Fill Rules

- Start from `magicpay plan-fill` on the current page, not from old
  assumptions. Use `--planner-hint <text>` only for short human-readable
  context when needed.
- Do not apply a stale plan after page changes.
- Keep the plan request small: purpose/options only, never raw values, target
  matches, Memory catalogs, materializers, browser writers, or page target
  lists.
- Treat `payment_card.authorization_required` as a non-blocking Memory
  availability state: the card exists, but provider-backed card handles remain
  hidden until `authorize-payment` succeeds in the active session. The advisory
  alone is not an authorization trigger: the current plan must contain
  protected card fields. An outer support/donation control opens the actual
  payment form first, then the new plan becomes the authorization boundary.
  Never ask for raw card details or route around this state through lower-level
  materialization calls.
- Run exactly the `applyCommand` returned by `plan-fill` to fill and stop before
  final commitment controls.

<!-- magicpay-continuation:v1 id=guardrails-plan-apply action=plan-apply -->
After `magicpay plan-fill`, execute its exact returned `applyCommand`.
<!-- /magicpay-continuation:v1 -->
- Use `magicpay fill-field` only as value-free recovery when the higher-level
  plan/apply path missed a visible field or chose the wrong target. The agent
  may bind one Memory field ref to one observed target id; it must not pass raw
  values.
- If Memory candidates are ambiguous, explain the displayed candidate facts to
  the user and submit the selected `choiceId` with
  `magicpay choose-memory --choice <choiceId>`. Do not use labels or list
  positions as CLI selectors.
- If MagicSearch returns `choice_required`, share the returned tokenized
  `requestUrl`, then immediately poll with
  `magicsearch choose --request <requestId> --json` until the UI choice
  resolves. Use this only for actual user-facing purchase options. If the
  request is asking the user to choose between providers or tool profiles, do
  not show that choice; rerun MagicSearch with `--choice-policy never` and
  continue with the automatically selected target. For Google Flights/Fli, run
  `magicsearch discover` with extracted flight slots before browser handoff so
  any choice request contains real itineraries, not providers. Do not stop after
  sharing a valid user-facing choice link or ask the user to come back to chat
  after choosing in the UI. If the user chooses from chat-displayed safe option facts
  instead, submit the selected backend-owned id with
  `magicsearch choose --request <requestId> --choice <choiceId> --json`. Do not
  use labels or list positions as CLI selectors, and do not silently pick for
  the user.
- If apply reports that the page changed, refresh the page state and rerun
  `magicpay plan-fill` before retrying.

## Protected-Action Rules

- Start typed action commands only when an active product session
  exists.
- Before `authorize-payment`, collect visible `amount`, `currency`,
  `recipient`, `country`, optional `description`, and optional `recurring` from the
  current page and the user's task.
- Follow the closed normal-checkout `magicpay authorize-payment --amount <live amount> --currency <live currency> --recipient <live recipient> [--description <live description>] [--recurring <live boolean>] --return-pending` command; keep country in the comparison record outside the command, never add `--country`, and keep missing live facts unknown until the checkout supplies them.
- Prefer merchant/payee names over payment processor names. Use page title,
  host, or URL only as supporting signals unless they clearly identify the
  merchant.
- Ask the user when amount, currency, merchant/payee, recurring status,
  country, or task/page facts are missing, conflicting, or ambiguous.
- Use that closed `magicpay authorize-payment` shape for payment authorization.
- Use `magicpay sign-message --item-ref <walletItemId> --message <text>` for
  wallet message signing, and ask again if the message changes.
- Use `magicpay confirm-action --summary <text> [--details <text>]` only for
  consequential actions without a more specific typed command.
- Keep `itemRef` on the existing selector path. Do not put it inside
  `params`, and do not change how MagicPay discovers or selects Memory items.
- Always add `--return-pending` to the typed action command and give the user
  the returned tokenized `requestUrl`. Relaying that link is the user's only
  reliable delivery: request notifications go out over push or Telegram and
  are suppressed on email, so a terminal-only user is never notified. Then
  immediately run the exact returned `pollCommand`; do not
  ask the user to tell you after they approve. Polling observes decisions made
  through the public link, admin, mobile app, or any other MagicPay UI. The
  active MagicPay profile supplies the local or hosted-development origin.
- For `authorize-payment`, tell the user they can approve in MagicPay UI with
  the link or send the one-time code from the MagicPay email. Run the exact
  returned `confirmOtpCommand` only for the code path, then resume the exact
  returned `pollCommand` after OTP confirmation.
- For `confirm-action`, `sign-message`, Memory choices, and Memory secret
  forms, use the link only. For Memory request links from `apply-fill`, run the
  exact returned `pollCommand` (`magicpay wait-memory`), not `wait-request`. Do not ask for OTP; codes
  apply only to payment approvals.
- Every approval polls the same way, whatever its kind. When a command reports
  a waiting decision, run the exact returned `pollCommand` in the same turn,
  right after giving the user the link. Never end a turn
  having asked the user to approve without also starting the poll, and never
  treat a chat reply as the signal to begin: polling observes the decision
  from the link, admin, mobile app, or any other MagicPay surface, so waiting
  to be told leaves both sides waiting for each other.
- After acknowledging approval detection, do not start `magicpay plan-fill`, an
  `applyCommand`, or long Memory work while the poll is merely `approved` or
  `executing`. Wait until the same attached `pollCommand` returns a ready or
  terminal result. Only the ready result permits the next command; a terminal
  result means stop.
- Browser commands and request polls have separate wall clocks: browser work
  returns before the standalone poll starts. Never nest an approval's lifetime
  under a browser-action deadline or interpret a browser timeout as a request
  decision.
- Do not print, log, summarize, save, or repeat OTP digits. Treat them as
  sensitive user input.

## Secrecy And Safety

- Never type, print, summarize, or log protected values manually.
- Never type, print, summarize, or pass card PAN, CVV, wallet private keys,
  passwords, or other protected values through action params.
- Do not pass **protected** Memory values (login credentials, card data, and
  fields stored as `secret`) through chat, logs, reports, summaries, or public
  command arguments. For an ordinary `chat_question`, pass the raw reply only
  through stdin to the exact returned `memory-reply` command. Never echo it,
  put it in argv, or construct `apply-fill --decision-json` values yourself;
  raw replies and mapped values never belong in logs, telemetry, or reports.
- Never print, log, summarize, or share `MAGICPAY_API_KEY`, local config, or
  CDP endpoints. Memory item ids may be passed between MagicPay commands as
  operational refs, but never show them to the user or external services.
- Never include OTP digits in logs, reasoning summaries, saved notes, task
  reports, or command summaries.
- Base progress claims on the visible form state.
- Base post-submit success claims on a fresh observed result page, not on the
  click/submit action itself.
- Treat merchant confirmation and provider settlement as separate facts. A
  merchant-success page may complete the workflow, but `pending` remains
  `pending` until MagicPay observes an actual provider success.
- After page-level changes, rerun `magicpay plan-fill` before acting on old
  fill plans.

## Ask The User When

- a browser-dependent step is needed but there is no browser child and neither
  `magicpay launch` nor an approved private CDP endpoint is available;
- the browser process to attach was not explicitly approved for this task;
- the next step would submit, login, purchase, send identity data, change an
  account, run a protected action, or otherwise commit a consequential action,
  and there is no matching typed approval for the unchanged current facts;
- payment authorization facts are missing or ambiguous: final amount,
  currency, merchant/payee recipient, recurring status, country, or a conflict
  between the user's task and the visible checkout page;
- Memory planning remains ambiguous or unavailable;
- approval reaches a terminal blocked state;
- client-side validation or merchant-specific recovery needs a human choice.

Never run `magicpay commit` while `apply-fill` last reported `waiting_for_user`
or `blocked`. Those mean the form is unfinished — an ask-before-use decision is
outstanding, or a write did not land — and the unwritten fields are the ones
the provider will refuse on. `commit` now refuses in that state
(`fill_incomplete`) without clicking anything. Resolve the pending request,
run exactly its returned `resumeCommand`, and commit only once that command
reports the form filled.

A provider's validation message often renders inside its own iframe and does
not reach the click's progress evidence, so a refusal can arrive looking like a
submission. When `commit` returns `commitment_blocked_by_empty_required_field`,
the page is still showing a required field with no value: nothing was charged,
so fill it and commit again rather than polling `payment-result`.

## Trust Model And Command Narration

MagicPay hides stored raw values from the
calling model; it does **not** make an untrusted runtime safe. If the browser,
OS, or shell is compromised, MagicPay alone does not protect against that.

MagicPay also cannot protect secrets that the user already typed into the
agent chat. The safest path is to use saved MagicPay Memory or a MagicPay
request path that keeps raw values out of the agent prompt.

Several agent chat surfaces render every shell execution as a bare
"Running command" row that hides what is happening. Before each `magicpay`,
`magicsearch`, or `magicbrowse` command, write one short plain-language line
in chat saying what you are about to do — "Verifying the one-time code",
"Checking the MagicCard balance". Describe the action only: never paste the
command, its subcommand, flags, or argument values into chat. Command
strings, challenge tokens, OTP codes, and API URLs belong in the tool call,
not in the conversation.

## Rare And Failure Guardrails

> **The MagicPay CLI is the only MagicPay surface in a product workflow.** Do
> not use app/connector MCP tools such as `magicpay_app.*`: they authenticate a
> separate ChatGPT OAuth session and do not know the CLI session, reservations,
> or approvals. A CLI failure stays in the CLI request model (`wait-request`,
> `list-memory-items`, `fill-field`) or stops with a report. Never switch
> MagicPay interfaces mid-workflow or edit installed CLI/SDK files as a fix.

> **Plan the browser process and page-control path before page preparation.**
> MagicPay fills and authorizes only in its launched child or an approved
> private CDP browser attached to the active session. The browser process must
> already expose CDP; an ordinary open desktop browser cannot gain it without
> restart, regardless of its controller. Confirm an endpoint before preparing
> the page. If none exists, run `magicpay launch` and prepare that child through
> a controller connected to the same endpoint.

> **Slow commands are still running, not broken.** `plan-fill`, `apply-fill`,
> `commit`, `act`, and the wait/poll commands can outlive your shell tool's
> output window. Empty or truncated initial output means the command is STILL RUNNING:
> fetch its pending output. Never rerun `plan-fill` or `apply-fill`
> because output looked empty or non-JSON; that creates a new plan identity and
> can repeat an approval. Preserve each pending request's exact id and returned
> `pollCommand`; run the exact returned `pollCommand` after interruption and
> never replace the request.

> **Request handoff is link-first.** Every pending Memory request, choice,
> secret form, and non-payment approval gives the user its tokenized
> `requestUrl`. Payment approval offers that link or, only when returned, the
> email OTP path. OTP is only for `authorize-payment` requests. Direct every
> non-payment request, including an unsolicited OTP, to its link.

> **Credential and browser authority are sensitive.** Do not print, log, or
> share `MAGICPAY_API_KEY`, MagicPay config, or CDP endpoints. Pass Memory refs
> and item ids only between commands that require them; never expose them to the
> user, reports, or external tools. `magicpay attach` accepts only the private
> browser the user approved for this task and only inside the active session.
> On a shared or compromised machine, stop and request key rotation/revocation.

> **Browser cleanup is separate.** MagicPay owns the protected workflow, not
> the browser. `magicpay close` closes or clears the browser child while
> keeping the session active. `magicpay end-session` completes the workflow but
> leaves teardown to the browser owner unless the user approved cleanup.

> **Canceled workflows need explicit cancel.** If the user says to cancel,
> abort, stop, or abandon the purchase—or a hung approval blocks cancellation—
> run `magicpay end-session --cancel` after any needed browser-child cleanup. It
> cancels unresolved waiting, approved, or executing requests server-side. Do
> not use it for timeouts, ordinary disconnects, or completed purchases.

> **Report final visible price on completion.** If the final amount, currency,
> or merchant is visible when the session ends, pass those facts to
> `magicpay end-session --amount-total <number> --currency <code>
--merchant-name <name>`. Do not invent a price, and do not treat
> `end-session` as approval or submission. After a fresh observation shows
> merchant acceptance, run `magicpay payment-result`; only `succeeded` is
> provider-backed success. For `pending` or `unknown`, follow `nextAction` and
> never invent a missing `pollCommand`. For recoverable failure, share the exact returned user copy and
> link, then immediately run the exact returned `recovery.pollCommand`. Never
> retry automatically or infer settlement from the merchant
> page. Use `provider_confirmed` only for `payment-result: succeeded`.

> **Memory plans stay value-free.** `magicpay plan-fill` observes the current
> page and matches value-free Memory descriptors to fields. Never give it raw
> values, precomputed matches, catalogs, materializers, or browser writers. If
> matching is unavailable, fail closed and report that state.

> **Provider-backed cards need payment authorization before reveal.**
> `magicpay plan-fill` may report a non-blocking blocker with
> `kind: "payment_card.authorization_required"` when a card exists but the
> active session cannot reveal its handles. Never inspect, infer, print, or ask
> for PAN/CVV. The advisory alone does not trigger authorization: require card
> fields in the current plan; guarded-commit and re-plan an outer support step
> first. Use the closed normal-checkout command; keep country in the comparison record outside the command, never add `--country`, and keep missing facts unknown. After authorization rerun
> `plan-fill` and its exact `applyCommand`; retain a recurring plan for combined
> payment/subscription approval.

> **CAPTCHA solving is recovery-only.** Only call
> `magicpay solve-captcha [--timeout <s>]` when a real CAPTCHA is confirmed
> on the current browser child. Never use it for waiting or detection. Only
> `fullyResolved: true` with `merchantCleared: true` and `outcomeType:
> "resolved"` permits continuation. `solverVerified` alone is not merchant
> clearance.
> After full resolution, get fresh visible page state from the current
> page-control owner. Do not invent or run a page-state CLI such as
> `magicbrowse get-page-state`; that command is not documented. Obtain fresh
> visible state only through the existing page-control owner's documented
> continuation. If an old checkout plan is involved, rerun `magicpay plan-fill`
> and execute its exact returned `applyCommand`. No `magicpay observe` command
> is documented in this bundle. CAPTCHA clearance alone does
> not authorize `magicpay commit`; commit only at the normal matching-approval
> and current-live-facts boundary. If
> MagicBrowse owns it, run `magicbrowse mark-captcha-resolved` before the next
> `magicbrowse act "continue..."`. `fullyResolved: false` or `outcomeType:
> "partial"` is not clearance: stop without marking or committing. Continue an
> already-returned provider reconciliation after a dispatched final click.
