## Description:

Searches and analyzes TikTok Shop seller data across supported marketplaces, returning store-level sales, GMV, audience, rating, product, influencer, video, livestream, and trend metrics for seller discovery and benchmarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, cross-border sellers, marketers, and ecommerce analysts use this skill to find and compare TikTok Shop stores by marketplace, category, GMV, sales trend, listing date, local or cross-border status, and sales channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox API credentials and sends TikTok seller query parameters to LinkFox endpoints.

Mitigation: Install and run only when the user is comfortable sharing those credentials and query data with the LinkFox service.

Risk: The skill can save full seller analytics responses locally, which may include commercially sensitive research data.

Mitigation: Review the local linkfox session output directory before sharing workspaces, logs, or generated artifacts.

Risk: The artifact includes account login, API-key generation, payment-order creation, and billing workflows.

Mitigation: Require explicit user approval before handling phone numbers, SMS codes, API keys, plan selection, payment methods, or order creation.

Risk: The security scan verdict is suspicious due to credential handling, local persistence, payment workflows, and automatic feedback reporting.

Mitigation: Review the skill and scan evidence before deployment, and monitor calls that report feedback or interact with account and billing endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-seller)
- [EchoTik TikTok seller list API reference](references/api.md)
- [Authentication and billing onboarding guide](references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, configuration guidance]

**Output Format:** [Markdown summaries and tables, saved JSON response files, and inline shell commands or configuration snippets when authentication or billing setup is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session directory; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
