## Description:

Queries EchoTik data so an agent can retrieve and present TikTok Shop new product rankings across 16 regional markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and agents use this skill to discover recently listed TikTok Shop products that are gaining traction and to inspect daily ranking metrics such as sales, revenue, creator activity, ratings, and prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags this as a paid LinkFox/EchoTik integration that can read API keys from environment variables and write full API responses locally.

Mitigation: Install only when that data flow is acceptable, keep LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY private, and treat saved response files as sensitive.

Risk: The onboarding flow can collect phone and SMS login details, generate API keys, and initiate payment-order flows when credits are missing.

Mitigation: Prefer the self-service key path when possible, confirm billing choices with the user before ordering, and avoid storing generated keys in shared shells or logs.

Risk: Environment-variable overrides can change LinkFox service endpoints.

Mitigation: Avoid running with untrusted LINKFOX_* base URL overrides and review the environment before execution.

## Reference(s):

- [EchoTik-TikTok新品榜 API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-new-product-rank)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and guidance, with JSON API responses saved locally by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a date, supports regional market and pagination parameters, uses paid credits, and may write full response data under a local linkfox session directory.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
