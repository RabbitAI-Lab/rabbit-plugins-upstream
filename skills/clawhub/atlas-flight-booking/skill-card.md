## Description:

Use when a user asks what Atlas Flight Booking can do, wants to authorize Atlas, search or compare flights using exact or flexible dates and time preferences, verify a current fare, choose baggage or seats, create and pay for an order, or check ticketing status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atlas-doc](https://clawhub.ai/user/atlas-doc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel operators use this skill to search exact or flexible-date flights, compare offers, verify current fares, select optional baggage or seats, and complete Atlas booking flows with explicit checkpoints for authorization, price increases, seat fallback, and payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags automatic installation or upgrade of local tooling, including remote uv installer scripts and the Atlas flight CLI, without a separate conversational permission step.

Mitigation: Review and approve the install behavior in the host execution environment before using the skill; allow only trusted uv and Atlas CLI sources and monitor native execution prompts.

Risk: Flight booking can create orders, initiate balance payment, or continue ticketing after user decisions.

Mitigation: Require the documented checkpoints: explicit authorization completion, fresh approval for price increases, a selected seat fallback policy, and explicit approval of the current masked payment summary before payment.

Risk: Passenger and contact data are sensitive and may be required for order creation.

Mitigation: Collect only CLI-required fields, send passenger data once through stdin or a user-supplied absolute file path, and do not echo, save, log, or place personal values in command arguments.

Risk: Uncertain order creation or payment results could cause duplicate side effects if retried.

Mitigation: Do not retry order creation or payment; use order status queries only when an order number is available.

## Reference(s):

- [Safe Booking Workflow](references/booking-workflow.md)
- [Atlas Flight Booking CLI Contract](references/cli-contract.md)
- [Passenger Input](references/passenger-input.md)
- [Atlas Error Handling](references/error-handling.md)
- [ATRIP price comparison documentation](https://resources.atriptech.com/api-wen-dang/api-reference/booking-apis/price-compare-search#price-compare-search)
- [uv installation documentation](https://docs.astral.sh/uv/getting-started/installation/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Atlas CLI commands, normalized status summaries, and JSON-handling rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs preserve opaque IDs, avoid exposing passenger data, and require explicit user confirmation before price increases, seat fallback policy, and payment.]

## Skill Version(s):

0.3.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
