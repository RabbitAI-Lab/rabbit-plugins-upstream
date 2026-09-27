# Troubleshooting

## Authentication expired or failed

Your MCP client will prompt for sign-in again. Complete it, then retry the tool call. Starting a purchase and answering a clarification require the `payments:write` scope; polling requires `payments:read`. If a purchase tool is rejected for insufficient scope, disconnect and reconnect Axiom so the client requests the current scope set.

## `account_setup_required`

The user is missing a verified email, a linked card, a phone number, or a shipping address. Relay `userMessage` and `setupUrl`. Do not call `make_purchase` again until the user says setup is complete.

## `needs_clarification` keeps coming back

The resolved fields are still ambiguous. Ask the user for the exact missing detail named in `question`, fold the answer into `itemName` (or `merchant`), and call `make_purchase` once more. Do not loop on `make_purchase` without a new answer; attempts are limited.

## `limit_reached`

Relay `userMessage` exactly. Do not retry, reword the request, or estimate a reset time.

## `mandate_denied`

The request did not pass Axiom's intent or purchase-policy check (for example, a merchant or product outside Axiom's policy, or a command that was not clearly a request to buy). Relay the reason and stop. Do not retry the denied request.

## `awaiting_approval` and polling

Send the `approvalLink` and stop polling. The user reviews and approves the order in Axiom. Polling again within 20 seconds returns `polling_too_often`; it does not speed anything up. Wait for the user.

## Purchase `failed`, `cancelled`, or `human_needed`

Normal terminal outcomes. Relay `userMessage` (it includes the reason when one is safe to share and the Axiom link). Ask the user how they want to proceed.

## Tool call returned `isError: true`

A transport or validation error, not a purchase outcome. Read `error` and `message`, fix the input (for example, a missing `browserPurchaseSessionID` or an invalid merchant URL), and retry once. If it persists, tell the user Axiom is temporarily unavailable.

## Wrong session or transaction

`get_purchase_status` says the browser purchase was not found: verify the `browserPurchaseSessionID` from the `make_purchase` response, or recover it via `list_transactions` (`purchaseFinality.browserPurchaseSessionID`).
