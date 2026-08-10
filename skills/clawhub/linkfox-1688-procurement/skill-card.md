## Description:

Helps LinkFox users run authorized 1688 procurement workflows, including OAuth checks, SKU and address lookup, order preview, guarded order creation, payment link retrieval, tracking, cancellation, receipt confirmation, and invoicing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement operators and agents use this skill to complete authorized 1688 purchasing tasks through LinkFox, from authorization and order preparation through payment-link retrieval, logistics tracking, cancellation, receipt confirmation, and invoice application. The skill is intended for request-by-request assistance rather than unattended end-to-end purchasing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate procurement, payment-link, cancellation, receipt-confirmation, invoice, account onboarding, API-key generation, and billing-plan flows.

Mitigation: Require explicit user confirmation for order creation, payment-link retrieval, cancellation, receipt confirmation, invoice application, and plan-purchase actions.

Risk: Flexible credential-bearing network calls can expose procurement or account data if pointed at untrusted hosts.

Mitigation: Verify LINKFOX_* base URL environment variables point to official LinkFox hosts before use and treat generated API keys as secrets.

Risk: Procurement actions may consume credits and repeated retries can increase cost.

Mitigation: Avoid automatic retries or polling after failures, empty results, incomplete parameters, or authorization issues; explain possible additional cost before continuing.

Risk: Onboarding and billing recovery flows can reveal sensitive account details in shared logs.

Mitigation: Avoid running onboarding in shared logs and redact API keys, tokens, full addresses, phone numbers, and payment URLs from user-facing output and feedback.

## Reference(s):

- [1688 Procurement API Reference](artifact/references/api.md)
- [1688 Procurement Workflow](artifact/references/workflow.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-procurement)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with Python command examples and JSON script responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses may be saved as redacted JSON files; high-risk write actions require separate user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
