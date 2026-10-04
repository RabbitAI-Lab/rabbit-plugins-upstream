## Description:

Guides agents through discovering and paying x402 or MPP services through the Nevermined Router within a delegated spending budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agents use this skill to find payable services, request a price, make capped purchases, and reconcile spending without a separate merchant account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can spend funds from an authorized buyer wallet.

Mitigation: Start in sandbox, use a strict Delegation cap, quote before paying, and set a per-call maximum.

Risk: Retries or bypassing an exhausted budget can cause unintended additional purchases.

Mitigation: Reuse a stable request ID for each purchase and stop on cap or insufficient-funds refusals; ask a human before increasing the budget.

Risk: Routed requests may disclose sensitive data to external services.

Mitigation: Exclude secrets and unrelated personal data from routed bodies and headers, and prefer catalog slugs over raw service URLs.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined app (API keys)](https://nevermined.app)
- [Service discovery](references/discovery.md)
- [Delegation and wallet setup](references/bootstrap.md)
- [Paying and quoting](references/paying.md)
- [Errors and guardrails](references/errors.md)
- [Payment ledger](references/ledger.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with HTTP and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Nevermined API key and a funded, capped Delegation for purchases.]

## Skill Version(s):

0.1.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
