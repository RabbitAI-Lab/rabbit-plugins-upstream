---
name: "discord-recipient-safety"
description: "Discord DM or relay recipient binding: authenticate the requester, validate the recipient, and require agent-sent requester attribution before every recipient-specific send."
---

# Discord Recipient Safety

Use before every recipient-specific Discord DM, relay, handover, report, assessment, or confidential-content send. Use it after the forwarding workflow has assembled content and before it calls the Discord message tool.

Each agent is a separate trust domain. The agent owns its credentials and sends under its own identity. Approved engineers may instruct that agent to relay, but the recipient must be told which approved engineer requested the relay.

## Boundaries

- Resolve both requester and recipient only from this agent's active approved roster; never from memory, prior DMs, display names, search results, or inferred routes.
- Keep names, Discord IDs, roster locations, and organisations out of this shared skill. Put them in the per-agent control manifest.
- Do not record message bodies, secrets, tokens, or unnecessary personal data.
- This skill cannot independently query Discord or intercept arbitrary message sends. A platform wrapper or before-tool policy hook must supply the non-content delivery evidence below.

## Required Inputs

Obtain one explicit requester instruction for one recipient. The request object includes the host-derived requester Discord identity, instruction event ID, exact requested recipient text, intended target, and content classification. Load this agent's approved roster and relay-pause state. Missing, malformed, or unavailable control input blocks the send.

## Pre-Send Procedure

1. Run `node scripts/recipient_safety.mjs pre-send --roster <approved-roster.json> --pause <relay-pause.json> --request <request.json>`.
2. Send only when the helper returns `PASS`.
3. Build the outbound body with `binding.attributionPrefix` immediately before relay content. The prefix identifies the approved requesting engineer; the agent remains the Discord sender.
4. Use `binding.exactMessageTarget` unchanged as the Discord message target.
5. Persist the binding record without the message body.

The helper blocks missing/non-exact instructions; unapproved/inactive requesters; zero/multiple recipient matches; inactive recipients; malformed/mismatched targets; and active or unknown pause state.

## Attribution Contract

Every forwarded body begins with a deterministic, non-secret attribution such as `Requested by <canonical requester name>:`. Do not claim the requester is the sender. Do not disclose a requester outside the approved roster, and do not send when attribution cannot be built from the passed binding.

## Send And Receipt

After a successful tool response, the wrapper records only non-content evidence: `exactMessageTarget`, `requesterDiscordUserId`, `attributionPrefix`, platform message ID, and delivery result. Run `node scripts/recipient_safety.mjs receipt --binding <binding.json> --delivery <delivery.json>`.

Only a `PASS` receipt permits a delivery claim. The helper verifies that the supplied target, requester attribution, and prefix exactly match the passed binding. It does not claim independent inspection of Discord's message body. Retain only requested recipient, canonical recipient, target ID, platform message ID, and delivery result.

## Misdelivery Response

After a confirmed misdelivery, set this agent's durable relay-pause state to active. Block later relays from this agent until a new explicit requester instruction is supplied and the pause is cleared through the incident procedure. Do not delete, resend, or contact any person automatically.

## Integration Contract

- The forwarding workflow supplies content and requester instruction; this skill supplies the requester/recipient binding gate and attribution prefix.
- The approved roster follows `references/approved-roster.schema.json` and is scoped to one agent/machine.
- A platform-level enforcement option is an OpenClaw `before_tool_call` hook that rejects recipient-specific message sends without a fresh passed binding. Verify the hook with non-production fixtures before enabling it.

## Validation

Run `node scripts/test_recipient_safety.mjs` before release. It covers successful attributed routing and receipt; target mismatch; receipt target or attribution mismatch; ambiguous recipient; inactive recipient; unapproved requester; missing receipt; and active pause.

## Acceptance Criteria

A recipient-specific Discord relay is complete only when requester authentication, recipient binding, required attribution, and post-send receipt all pass. A missing or blocked receipt means delivery is unconfirmed.
