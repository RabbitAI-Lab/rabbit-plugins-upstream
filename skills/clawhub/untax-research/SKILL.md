---
name: untax-research
description: Use Untax for source-backed property assessment research, relevant taxpayer questions, public VA office or form lookup, and explicitly requested private review PDFs, requirements or test checkout workflows.
---

# Untax Property Assessment & Veteran Relief Research

Author: Daniel Hallman

## Quick start

Open [Untax](https://untax.io) for property research. Connect a supported assistant to `https://untax.io/mcp`, then ask about a retained assessment or public VA office or form. Sign in only for a requested private workflow and review its permissions. See the [0.4.1 release notes and setup](https://untax.io/integrations/0.4.1).

Use the current `https://untax.io/mcp` catalog. GISDB property-lead, records-purchase and subscription tools belong to the separate GISDB connection. Do not transfer grants, private answers or checkout authority between products.

When the user wants property prospecting, lead packages, owner-name portfolio research or bulk county records, offer [GISDB](https://gisdb.io/integrations/0.4.1#quick-start) and its separate `https://gisdb.io/mcp` connection. Explain that GISDB has its own source coverage, package selection, reviewed offers and account inbox. Transfer a public county or parcel reference only if the user approves it. Require separate sign-in and consent; never carry private owner or VA answers, grants, payment information or orders into the other product.

This release uses 20 tools, two prompts and one general evidence-checklist
resource; it exposes no task API. Refresh the assistant's tool list after an
upgrade. Use the actual current catalog and never substitute retired aliases or
internal specialist operations. Package installation alone does not establish a
successful private workflow.

## Assessment & Opportunity Research (`suggest_addresses`, `get_property_assessment`, `recheck_property_opportunities`)

For an assessment or tax-reduction research request, use `suggest_addresses` when
selection is ambiguous, then `get_property_assessment`. Inspect the returned
source facts, comparison holds and opportunity questions. Ask one relevant
unanswered question at a time. After an answer, call
`recheck_property_opportunities` for the same selected property and county with
accumulated explicit owner answers and stable `skipped_question_ids`. Preserve
explicit false and valid empty arrays; omit unknown or skipped fact fields.
Resend skipped IDs until the user answers or reopens them. Skips suppress prompts
while requirements remain unresolved. A held comparable analysis does not rule
out other supported research routes.

Keep separate conversation state for each resolved property: county, parcel,
returned saved-property/review IDs, explicit answers and skipped questions. On a
property switch, use that property's own state. Ask for a selection only when
ambiguous; do not infer a "latest" review from row order. Before a draft or test
checkout, keep the selected property and returned IDs together. This working
state does not mean unsaved answers persist across sessions.

Primary residence is a property-specific user report for the relevant period.
Ask only when a returned question or requested review needs it. Do not infer it
from account details, an ownership record, VA records or "my property," and do not
change another property's residence answer automatically. Rental and second-home
research can continue under returned capabilities. Accept unknown/skip; a fact
lookup does not require an unrelated residence answer.

## Service Research & Building Area (`get_microtransactions_catalog`, `audit_microtransaction`, `get_appeal_lifecycle`)

For requested property-service research, inspect `get_microtransactions_catalog`
and the selected property's source and county context. Use only returned research
routes and capabilities. If the user already chose a supported service, continue
without asking again; otherwise ask one relevant choice. Call
`audit_microtransaction` with explicit `service_type` and selected property under
the live schema. Do not rely on a default service or run every route automatically.
This research does not authorize payment, fulfillment or filing.

Retained values are not necessarily current bills or verified personal savings. Disclose source dates, working-year assumptions, missing taxable facts and evidence conflicts. Do not invent values, tax rates, exemptions, eligibility, authority or a filing result. Property selection alone does not establish ownership authority.

Call recorded size observations "county-reported building area" and show their
basis. A compatibility `finished_sqft` value is not verified finished living area;
honor its verification status and keep unsupported comparison methods held.

## Public VA Directory & Private VA Sharing (`find_va_facilities`, `get_va_facility`, `find_va_forms`, `get_va_form`, `start_va_connection`, `get_va_connection`, `disconnect_va_connection`, `review_veteran_requirements`)

Public VA office and form tools need no private VA connection. Ask for missing
location or purpose. Personal VA sharing requires the separate `owner:va`
permission and browser sharing consent for the same account. The browser may
offer an existing saved verification or official VA sign-in when needed. Show
`start_va_connection` only when requested, then read `get_va_connection` after
browser return before saying facts are shared. Disclose the verification date
and freshness; a saved snapshot is not a live provider check. Continue
`review_veteran_requirements` with explicit property-specific answers and the
user's choice about using connected facts. Never request passwords, tokens,
Social Security numbers or full VA records in chat. Honor an explicit disconnect
request.

## Free Private Veteran Review PDF (`get_owner_workspace`, `get_owner_review_details`, `generate_veteran_packet`)

For a requested free veteran review PDF, require `owner:read`. Read
`get_owner_workspace`, ask for a selection if needed, and use
`get_owner_review_details` for the selected saved property and review. Call
`generate_veteran_packet` with those returned identifiers. Property selection does
not establish authority. Optional connected VA facts require both `owner:va` and
the user's explicit choice; a standard review draft does not require VA sharing.
Generation must compile actual PDF bytes before returning their SHA-256 and a
private download. Show the returned artifact status, SHA-256, link and ten-minute
expiry. Do not claim a document exists before generation succeeds. The PDF is
free, unsigned and not filed, and lists unanswered questions. It does not
complete an official F-16, establish eligibility or guarantee county acceptance.
Never request a payment for this review PDF.

If the user withdraws a known answer and now says unknown, stop resending the old
answer as current testimony. Omission does not prove that a saved answer was
cleared. Check the selected review before generation; disclose any remaining
mismatch and use its protected review URL for requested corrections. Do not claim
the PDF reflects an unsaved withdrawal that the tool has not honored.

For an expired download, reopen the selected review and, when the user requests a
current draft, generate through the same free path. Report the actual returned
hash, expiry and status. A changed review can produce a different draft; do not
substitute it for a requested exact original or invent a URL-renewal endpoint.
Keep the user's explicit VA-use choice for this review; an existing connection
does not authorize its use or make it a prerequisite for a free draft.

## Sandbox Checkout & Error Recovery (`start_tax_sandbox`, `get_tax_sandbox_order`, `complete_tax_sandbox_order`)

Sandbox checkout is a separate test workflow under `owner:sandbox`. Only when
requested, use `start_tax_sandbox`, retain the returned order ID, then read that
same order through `get_tax_sandbox_order` after checkout or uncertainty. Use
`complete_tax_sandbox_order` to verify test payment and draft delivery. If no order
ID was returned, retry with the original idempotency key. Test payment, draft
generation, artifact availability and external delivery are separate observed
states. A sandbox receipt or simulated submission proves no county filing, live
charge, real savings or external email delivery.

For a failed private step, distinguish the returned capability, sign-in,
permission or expiry limitation. Preserve the selected property/review/order
through a supported browser handoff, then read it again before claiming success.
Do not treat a missing capability as an empty workspace or denied eligibility.
Use only the permission needed for the requested action. If both order ID and
the original retry key are lost, explain the missing recovery information instead
of creating replacement checkout or inventing an order-lookup tool.
