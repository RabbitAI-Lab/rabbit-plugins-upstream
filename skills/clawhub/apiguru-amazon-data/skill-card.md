## Description:

Fetches live product, price, review, search, best-seller, deal, stock, and seller data from Amazon marketplaces through Apiguru.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT

## Use Case:

External users and shopping agents use this skill to retrieve live Amazon product, pricing, review, deal, stock, and seller information when requested, across 23 marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic retries of paid requests could cause extra charges without renewed approval.

Mitigation: Prefer free keyless access until paid-request retry handling is fixed. For paid calls, set provider-side spending limits and treat connection failures as potentially charged.

Risk: Feedback text is posted publicly.

Mitigation: Review feedback before posting and remove sensitive information.

Risk: Optional MCP components are outside the skill's audit.

Mitigation: Review optional MCP components separately before using them.

## Reference(s):

- [Endpoint reference](artifact/references/endpoints.md)
- [Errors, costs, and retries](artifact/references/errors-and-costs.md)
- [Apiguru API capabilities and pricing](https://agent.apiguru.app/.well-known/x402)
- [Apiguru payment documentation](https://agent.apiguru.app/llms-full.txt)
- [ClawHub skill release](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Publisher homepage from skill metadata](https://github.com/apiguru-app/agent-kit)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured marketplace data (JSON) with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live results vary by requested Amazon marketplace and data type.]

## Skill Version(s):

1.1.57 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
