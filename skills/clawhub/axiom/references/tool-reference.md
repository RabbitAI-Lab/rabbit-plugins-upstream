# Axiom MCP tool reference

Six tools. Money fields are in dollars unless the field name ends in `Cents` (for example the `maxTipCents` input), with one documented exception on `get_transaction` noted below. All IDs use the `ID` suffix (`transactionID`, `browserPurchaseSessionID`, `requestID`).

## `get_payment_method`

Returns the payment method saved in the user's Axiom account (brand and last 4 digits only) and whether account setup is complete. Optional before an order: `make_purchase` performs the same checks and its `running` response includes `paymentCard`. Use it when the user asks which payment method Axiom has on file.

- Parameters: none.
- Returns: `hasPaymentMethod`, `card {brand, last4}`, `accountSetupComplete`, `missingRequirements[]`, `setupUrl`, `userMessage`.

## `make_purchase`

Starts an order. Axiom verifies the request against the user's intent and spending rules, then completes the merchant's checkout on the user's behalf. Returns immediately.

- Parameters: `userCommand` (near-verbatim), `merchant {merchantName, merchantURL}`, `itemName` (with variants), optional `itemSubtotal` (dollars), optional `intentContext {resolvedUserIntent, evidence[], resolutionSummary}`, optional `preferences {fulfillment, substitutionsAllowed, maxTipCents, notes}`.
- Returns: `status` (`running`, `needs_clarification`, `unavailable`, `mandate_denied`, `limit_reached`, `account_setup_required`, or a terminal state), `nextAction`, `userMessage`, `agentInstructions`, `browserPurchaseSessionID` and `transactionID` when started, `paymentCard` when known, `question` and `options[]` for clarifications, `source` (`intent_sufficiency`, `purchase_request_resolution`, `review_demo_catalog`), `isFinal`, `safeToTellUserComplete`.

## `get_purchase_status`

Checks an order started by `make_purchase`. Waits up to 30 seconds for the next change, then returns. Call in a loop while `running`. Polling a purchase that is waiting on the user again within 20 seconds returns `status: polling_too_often` with the same `nextAction`, `userMessage`, and link or question: stop polling and wait for the user.

- Parameters: `browserPurchaseSessionID`.
- Returns: everything above plus `progressStage`, `progressLabel`, `approvalLink` (when `awaiting_approval`), `userInputRequest {requestID, question, reason, options[{optionID, label, description, amount, imageUrl, productUrl}], allowFreeText}` (when `awaiting_user_input`), and on completion `confirmation`, `receipt`, `cart`, `finalTotal`, `transactionUrl`. Every amount in this response, including `receipt.total` and each `receipt.items[].amount`, is in dollars.

## `submit_purchase_clarification`

Answers an `awaiting_user_input` question and resumes the same order. Not for `needs_clarification` or `unavailable` from `make_purchase`.

- Parameters: `browserPurchaseSessionID`, `requestID`, and `selectedOptionID` and/or `userInput`.
- Returns: the same shape as `get_purchase_status` (usually `running`).

## `list_transactions`

Recent transactions, newest first.

- Parameters: optional `limit` (1 to 100, default 20).
- Returns: `transactions[]` with `transactionID`, `status`, `merchant`, `amount`, `description`, `createdAt`, and `purchaseFinality` (includes `browserPurchaseSessionID`, `isFinal`, `safeToTellUserComplete`, `nextAction`) for browser purchases; plus `count` and `total`.

## `get_transaction`

One transaction with receipt, audit trail, approval state, and `purchaseFinality`.

- Parameters: `transactionID` (legacy alias `transactionId` also accepted).
- Returns: `transactionID`, `transactionUrl`, `status`, `merchant`, `amount`, `description`, `receipt {items, taxesAndFees, discounts, shipping, total, orderNumber}`, `approval`, `auditTrail[]`, `purchaseFinality`.
- Receipt units differ here: `receipt.total` is in dollars, but `receipt.items[].amount`, `receipt.taxesAndFees[].amount`, `receipt.discounts[].amount`, and `receipt.shipping.amount` are in cents, as stored. Divide those by 100 before quoting them, or read the dollar receipt from `get_purchase_status` instead.

## Field glossary

| Field | Where | Meaning |
|---|---|---|
| `userMessage` | every purchase-flow response | Text for the end user. Relay as written. |
| `agentInstructions` | every purchase-flow response | Guidance for you. Never show it. |
| `nextAction` | every purchase-flow response | One of `poll_get_purchase_status`, `open_approval_link_then_wait_for_user`, `submit_purchase_clarification`, `ask_user_then_call_make_purchase`, `tell_user_unavailable`, `tell_user_complete`, `tell_user_failed`, `tell_user_denied`, `tell_user_limit_reached`, `open_account_settings`, `none`. |
| `safeToTellUserComplete` | purchase responses, `purchaseFinality` | The only success signal. Must be `true` with `status: "completed"`. |
| `transactionUrl` | purchase responses, `get_transaction` | The Axiom page for this purchase. The link to share with the user. |
| `approvalLink` | `awaiting_approval` | Where the user reviews and approves the order in Axiom. Send it; poll again after they say they approved. |
| `progressStage` / `progressLabel` | `running` | Public progress: `starting`, `finding_items`, `checkout`, `shipping`, `delivery`, `payment`, `reviewing_cart`, `placing_order`, `receipt`. |
| `paymentCard` | `running` from `make_purchase`, when available | `{brand, last4}` of the payment method that will be used. Omitted when Axiom could not read the saved card in time; that does not stop the order. |
