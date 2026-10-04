# Worked examples

Each example shows the user's words, what the model does, and why.

## 1. Clear request: call directly

User: "Order a 25 lb bag of Acana Adult Recipe dog food from Chewy."

All four pre-flight boxes are checked (merchant, product, variant = size, intent to buy). Call `make_purchase`:

```json
{
  "userCommand": "Order a 25 lb bag of Acana Adult Recipe dog food from Chewy.",
  "merchant": { "merchantName": "Chewy", "merchantURL": "https://www.chewy.com" },
  "itemName": "Acana Adult Recipe dry dog food, 25 lb bag"
}
```

Response `status: "running"`. Relay `userMessage` (it names the payment method on file and the tracking link), then poll `get_purchase_status`.

No extra confirmation question is needed here: the user asked for a specific item, and Axiom applies their spending rules and requests their approval if the order requires it.

## 2. Vague request: ask first, do not call

User: "Get me some running shoes from On."

Product and required variants (model, size, width, color) are unknown. Do **not** call `make_purchase`. Ask one question:

"Sure. Which On model, and what size and color? If you have a product link, paste it."

Only after the user answers do you call `make_purchase`.

## 3. Terse contextual request: resolve from context, include evidence

Earlier in the conversation the user bought "Big Moods Possum Dumpster Fire Sticker" from bigmoods.com. Now: "Get that sticker again."

Resolve from context and pass `intentContext`:

```json
{
  "userCommand": "Get that sticker again.",
  "merchant": { "merchantName": "Big Moods", "merchantURL": "https://bigmoods.com/products/possum-dumpster-fire-sticker" },
  "itemName": "Possum Dumpster Fire Sticker",
  "intentContext": {
    "resolvedUserIntent": "User wants to reorder the Big Moods Possum Dumpster Fire Sticker they bought earlier in this conversation.",
    "evidence": ["Earlier turn: user asked to buy the Possum Dumpster Fire Sticker from bigmoods.com and the purchase completed."]
  }
}
```

## 4. Pre-mandate clarification: re-call `make_purchase`

`make_purchase` returns:

```json
{ "status": "needs_clarification", "source": "purchase_request_resolution",
  "question": "Which size?", "options": [{ "optionID": "m", "label": "M", "amount": 125 }, { "optionID": "l", "label": "L" }],
  "nextAction": "ask_user_then_call_make_purchase",
  "userMessage": "Before I can start this purchase, I need one more detail: Which size?\n1. M ($125.00)\n2. L" }
```

Relay `userMessage`. User says "Large." Call `make_purchase` again with `itemName: "… size L"`. Do not call `submit_purchase_clarification`; there is no session yet.

## 5. Approval

`get_purchase_status` returns `status: "awaiting_approval"` with `approvalLink` and `userMessage` "Your purchase of … for $123.45 needs your approval before it can be placed. Approve it here: https://app.useaxiom.ai/transactions/… Tell me once you've approved and I'll check on it."

Relay it and stop polling. The user reviews and approves the order in Axiom through the link; when they say they approved, call `get_purchase_status` again.

## 6. Mid-checkout question: `submit_purchase_clarification`

`get_purchase_status` returns `status: "awaiting_user_input"`, `userInputRequest.requestID: "browserpurchaseinput:1"`, options Black / White, and `userMessage` with the question and the numbered options.

Relay it. User says "Black." Call:

```json
{ "browserPurchaseSessionID": "browserpurchasesession:1", "requestID": "browserpurchaseinput:1", "selectedOptionID": "option-black" }
```

Then keep polling `get_purchase_status`.

## 7. Completion

`get_purchase_status` returns `status: "completed"`, `safeToTellUserComplete: true`, and `userMessage` "Your Chewy order went through. Confirmation number: 1234567. Total: $61.18. Receipt and details: https://app.useaxiom.ai/transactions/…"

Relay it, optionally with a one-line summary of `receipt.items`. Stop polling.

If `safeToTellUserComplete` is `false`, relay the `userMessage` (it says confirmation is still pending) and do not say the order went through.

## 8. Lost session ID

The conversation was long and you no longer have `browserPurchaseSessionID`. Call `list_transactions`, find the in-flight transaction, read `purchaseFinality.browserPurchaseSessionID`, and resume `get_purchase_status`.

## 9. Out of tool calls mid-purchase

You have polled five times and the purchase is still `running`. Relay the latest `userMessage` (progress plus the tracking link) and say you will check again when the user asks. On their next message, call `get_purchase_status` with the saved session ID.
