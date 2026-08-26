## Description:

Assists LinkFox users with authorized 1688 procurement, including OAuth checks, SKU and address lookup, order preview, guarded order creation, payment link retrieval, order tracking, logistics, cancellation, receipt confirmation, and invoicing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External LinkFox users and agents use this skill to complete authorized 1688 procurement steps while preserving required authorization checks and explicit confirmations for payment, order, receipt, cancellation, and invoicing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can touch procurement, account, billing, and feedback data through LinkFox services.

Mitigation: Install only when LinkFox is trusted for those workflows, and review payment or feedback actions before allowing the agent to proceed.

Risk: Generated API keys may be long-lived secrets.

Mitigation: Prefer the self-service API-key path when possible, keep API keys out of chat and logs, and rely on the skill's redaction behavior for outputs.

Risk: Endpoint environment variable overrides can redirect requests away from the expected LinkFox services.

Mitigation: Avoid overriding LinkFox endpoint environment variables unless the endpoint is controlled and trusted.

Risk: Order creation, payment-link retrieval, cancellation, receipt confirmation, and invoice application can affect real procurement state.

Mitigation: Require a separate explicit user confirmation for each high-risk action, stop on failed previews or authorization checks, and avoid automatic retries of write operations.

## Reference(s):

- [1688采购流程 API 参考](references/api.md)
- [1688采购流程地图](references/workflow.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-procurement)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and redacted JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses may be saved as redacted JSON files; high-risk actions require separate explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
