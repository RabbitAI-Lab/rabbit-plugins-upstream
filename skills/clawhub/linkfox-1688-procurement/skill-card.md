## Description:

1688采购全流程 helps LinkFox users run authorized 1688 procurement, including OAuth checks, SKU and address lookup, order preview, order creation, payment-link retrieval, order tracking, logistics, cancellation, receipt confirmation, and invoicing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External LinkFox users and procurement operators use this skill to manage authorized 1688 purchasing flows from account authorization through order fulfillment and invoicing. The skill is intended for supervised procurement workflows where high-risk purchase, payment, cancellation, receipt, and invoice actions are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account onboarding and credential handling may expose procurement access if configured in shared or synced shell profiles.

Mitigation: Install only when LinkFox is trusted for the procurement workflow, keep LINKFOX_* endpoint variables on official LinkFox HTTPS hosts, and avoid storing API keys in shared or synced shell profile files.

Risk: High-risk actions can create orders, retrieve payment links, cancel orders, confirm receipt, or apply for invoices.

Mitigation: Review each high-risk action in business terms and require a separate Chinese natural-language confirmation immediately before execution.

Risk: Unauthorized or expired 1688 account authorization can make procurement operations fail or target the wrong account state.

Mitigation: Check the current LinkFox user's authorized 1688 stores before procurement operations and re-authorize through the provided authorization flow when no active, unexpired store is available.

## Reference(s):

- [1688 procurement API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [1688 procurement workflow map](references/workflow.md)
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-procurement)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and shell command invocations with JSON script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [High-risk procurement actions require separate Chinese natural-language confirmation; large script responses may be saved as redacted JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
