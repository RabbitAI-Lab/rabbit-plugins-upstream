## Description:

Mines related Ozon and available Wildberries keywords from a seed term and returns marketplace metrics such as search volume, growth, competition, price, relevance, title density, cart-add conversion, and top products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agent users use this skill to expand Russian Ozon seed keywords, identify long-tail or low-competition opportunities, and review market profiles before further marketplace research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, SMS-login account flows, and marketplace query data.

Mitigation: Install and run it only when the user trusts LinkFox, and store credentials in a safer secret store rather than pasting API keys into shell profile files.

Risk: The skill can trigger paid credit consumption and payment/order flows.

Mitigation: Confirm the expected 12-credit cost before repeated calls, and require explicit user approval before any recharge or order action.

Risk: Full API responses and session metadata are saved locally under linkfox directories, with fallback paths possible outside the current project.

Mitigation: Review saved files after use, avoid sensitive seed terms in shared workspaces, and clean local response files when they are no longer needed.

Risk: Custom LinkFox endpoint environment variables can redirect requests.

Mitigation: Use default endpoints unless the destination is controlled and trusted by the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-keyword-mining)
- [Seerfar Ozon keyword mining API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and JSON summaries, with full API responses saved as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consumes 12 credits per call, uses a 24-hour local cache for identical parameters, and saves full responses under local linkfox session directories.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
