## Description:

Helps agents query EchoTik TikTok Shop new product rankings to surface trending new products across 16 regional markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and analysts use this skill to query daily TikTok Shop new product rankings, compare product performance, and identify emerging product trends by market.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox API access and handles API keys.

Mitigation: Prefer self-service API-key setup, avoid storing keys in shared shell profiles, and review any environment variables that can override LinkFox endpoint URLs.

Risk: Queries and onboarding flows can consume paid credits or initiate billing actions.

Mitigation: Confirm each paid query, plan selection, and order with the user before continuing.

Risk: Full API responses and feedback reports can disclose or retain user and query data.

Mitigation: Treat saved local response files and automatic feedback submission as data disclosure and retention points, and avoid sharing sensitive task details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-new-product-rank)
- [EchoTik TikTok New Product Ranking API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, shell commands, configuration steps, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
