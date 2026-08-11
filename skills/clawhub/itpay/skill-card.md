## Description:

ItPay gives OpenClaw agents a single CLI entry point for buyer workflows covering service discovery, purchase, checkout, delivery, recovery, and refunds, while seller workflows are not yet implemented.

This skill is ready for commercial/non-commercial use.

## Publisher:

[itpay](https://clawhub.ai/user/itpay)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run ItPay buyer workflows in OpenClaw, including finding services, presenting prices before checkout, completing delivery, handling recovery, and requesting refunds. Operators can use the packaged commands and guidance to keep the ItPay agent type, host target, checkout state, and recovery flow consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ItPay workflows can involve external service prices and checkout authorization.

Mitigation: Show the exact price and required contact fields before checkout, then wait for explicit human agreement before continuing.

Risk: Account-scoped order access can be exposed if ITPAY_BEARER_TOKEN is provided unintentionally.

Mitigation: Do not provide or set ITPAY_BEARER_TOKEN unless the operator intends account-scoped order access.

Risk: ItPay identity and checkout recovery state can remain under ~/.itpay-v3 after a session ends.

Mitigation: Treat local ItPay state as persistent identity and recovery material; do not copy, expose, rotate, or delete it to bypass normal recovery.

## Reference(s):

- [ClawHub ItPay skill page](https://clawhub.ai/itpay/skills/itpay)
- [ItPay OpenClaw skill homepage](https://github.com/itpay-ai/itpay-skill-openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and uses the bundled ItPay CLI for OpenClaw buyer workflows.]

## Skill Version(s):

2.0.25 (source: server release evidence and bundle.lock.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
