## Description:

Discover SameDayDesk's twenty-two account-free machine services and produce a verified, non-spending purchase intent from the live OpenAPI contract and unpaid HTTP 402 challenge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[epistemedeus](https://clawhub.ai/user/epistemedeus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover SameDayDesk paid machine services and prepare a verified purchase intent before a separately authorized payment executor is involved. It helps preflight public extraction, audits, enrichment, payment-offer checks, settlement evidence, and wallet-policy conformance without signing or sending payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts SameDayDesk and may disclose the public target the caller asks it to analyze.

Mitigation: Use only public targets intended for preflight analysis and review the selected operation before making the unpaid request.

Risk: A purchase intent could be mistaken for authorization to spend or proof that a paid service ran.

Mitigation: Treat the intent as point-in-time preflight evidence only; require a separate explicitly authorized payment executor for any payment action.

Risk: Runtime payment terms can change between discovery and execution.

Mitigation: Use the live HTTP 402 challenge as the authority for amount, network, asset, recipient, expiry, and resource before any later payment step.

## Reference(s):

- [SameDayDesk service origin](https://agents.samedaydesk.com)
- [SameDayDesk OpenAPI contract](https://agents.samedaydesk.com/openapi.json)
- [ClawHub skill page](https://clawhub.ai/epistemedeus/skills/samedaydesk-machine-commerce)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration, JSON]

**Output Format:** [Markdown guidance with a structured purchase-intent payload]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill stops before payment and reports credentialsUsed, paymentSigned, and paymentSent as false.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
