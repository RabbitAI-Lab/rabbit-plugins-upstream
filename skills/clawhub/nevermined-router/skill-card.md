## Description:

Helps agents discover, quote, and pay for external AI services through the Nevermined Router within a human-set budget, then review spending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent operators use this skill to find cataloged data, search, enrichment, inference, or scraping services, check a call's price, make a purchase within an approved spending cap, and review payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls can spend real money from the funded wallet through the spending delegation.

Mitigation: Review each quote, use a spending cap appropriate to the task, and check the payment ledger after calls or ambiguous failures.

Risk: The security scan was partial and could not resolve ten local references.

Mitigation: Review the skill's referenced material and external service destinations before use, and protect the Nevermined API key.

## Reference(s):

- [Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Commerce MCP documentation](https://nevermined.ai/docs/products/catalog/mcp)
- [Router guardrails and errors](https://nevermined.ai/docs/products/catalog/router/guardrails)
- [Bootstrap: API key, delegation, and funded wallet](references/bootstrap.md)
- [Discovering services](references/discovery.md)
- [Paying for services](references/paying.md)
- [Payment ledger](references/ledger.md)
- [Router errors](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the agent to make paid external service calls within a human-approved spending cap.]

## Skill Version(s):

0.1.45 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
