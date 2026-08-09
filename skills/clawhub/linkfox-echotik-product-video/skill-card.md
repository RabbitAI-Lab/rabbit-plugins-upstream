## Description:

EchoTik-商品视频查询 helps agents query promotional TikTok Shop videos for a product and summarize engagement, estimated sales, GMV, publish timing, and creator information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, analysts, and agents use this skill to inspect which TikTok videos promote a specific product, compare influencer content performance, and identify videos associated with higher estimated sales or GMV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox/EchoTik API credentials and may guide phone-based account login flows.

Mitigation: Install only when users intend to grant those credentials, keep API keys in environment variables, and rotate or remove keys when access is no longer needed.

Risk: The skill includes billing and payment helpers for credit purchases.

Mitigation: Require explicit user confirmation before plan selection or order creation, and review credit costs before continuing.

Risk: The skill stores complete API responses locally and can report feedback about skill behavior.

Mitigation: Treat saved result files as potentially sensitive, avoid sharing them unnecessarily, and prefer versions where persistence and feedback reporting are opt-in.

## Reference(s):

- [EchoTik Product Video API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-product-video)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown tables and JSON files, with stdout JSON or summaries from the bundled query script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under the workspace linkfox data directory; larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
