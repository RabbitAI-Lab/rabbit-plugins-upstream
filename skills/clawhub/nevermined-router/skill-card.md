## Description:

Guides agents through discovering and paying external x402 and MPP services with the Nevermined Router, including spending limits, price checks, and payment reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agents use this skill to find payable services, authorize bounded spending, estimate costs before calls, make paid requests, and audit the resulting payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous paid calls can spend real funds.

Mitigation: Test with sandbox keys; set small delegation caps and expiries, obtain a fee-inclusive quote, and limit each call's maximum total.

Risk: Untrusted payment targets or requests may expose funds or sensitive information.

Mitigation: Prefer catalog slugs; avoid raw proxy targets unless needed, and never send personal secrets or the Nevermined API key in merchant-bound requests.

Risk: Retrying an uncertain paid request may cause a duplicate charge.

Mitigation: Use unique request IDs and reconcile uncertain payments in the ledger before attempting another charge.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Router release on ClawHub](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined app and API keys](https://nevermined.app)
- [Agent Services Catalog](https://nevermined.app/catalog/ai-catalog.json)
- [Payment instructions](references/paying.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTTP and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Nevermined API key for paid calls; service discovery is public.]

## Skill Version(s):

0.1.31 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
