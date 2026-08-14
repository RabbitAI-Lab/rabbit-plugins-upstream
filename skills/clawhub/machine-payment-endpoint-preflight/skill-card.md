## Description:

Machine Payment Endpoint Preflight inspects one public HTTPS endpoint without credentials or payment, validates the URL, makes one bounded GET request, and reports whether HTTP 402 x402 or MPP payment offers are parseable and internally consistent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to preflight a public machine-payment endpoint before any payment flow by checking that its unpaid x402 or MPP offer data is parseable, internally consistent, and safe to evaluate further.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow contacts a public endpoint supplied by the user.

Mitigation: Inspect only public HTTPS URLs, make one bounded GET request, and do not include credentials, cookies, signing material, or payment authorization.

Risk: Payment-offer data could be malformed, inconsistent, expired, or unsafe to act on.

Mitigation: Treat the unpaid response as evidence, report parseability and internal consistency, and return a safe next action without signing, paying, or broadcasting a transaction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/machine-payment-endpoint-preflight)
- [AgentPMT workflow page](https://www.agentpmt.com/agent-workflow-skills/machine-payment-endpoint-preflight)
- [Data Format Validation tool skill](https://clawhub.ai/agentpmt/data-format-validation)
- [Webhook HTTP Request tool skill](https://clawhub.ai/agentpmt/webhook-http-request)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured endpoint preflight findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports protocols, prices, currencies, networks, recipients, expiries, conflicts, and a safe next action without signing, paying, or broadcasting transactions.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
