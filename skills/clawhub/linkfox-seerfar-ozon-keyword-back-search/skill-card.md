## Description:

Seerfar Ozon keyword back-search reverse-lookups Ozon and available Wildberries search keywords for up to 20 product SKU IDs, returning organic and advertising keyword metrics for listing optimization, competitor traffic-word discovery, and ad-word analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, ecommerce analysts, and agent users use this skill to reverse-look up search terms for Ozon product SKUs and compare organic, advertising, demand, competition, pricing, and conversion metrics. It supports SKU-driven keyword research for listing optimization and competitor traffic analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox account credentials and may touch account login, API-key, billing, and feedback workflows.

Mitigation: Install only when the publisher is trusted; prefer session-scoped API-key configuration and review onboarding or payment commands before running them.

Risk: Keyword lookup calls consume paid credits and repeated lookup attempts can increase cost.

Mitigation: Confirm user intent before additional paid calls, rely on the 24-hour local cache where applicable, and avoid automatic retries with changed parameters.

Risk: The lookup script writes full API responses to local session files.

Mitigation: Review the output path and stored response files before sharing or committing workspace contents.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-keyword-back-search)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [JSON response files plus stdout JSON or concise text summaries suitable for markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a session-scoped linkfox data directory; responses over 8 KB are summarized unless inline output is requested.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
