## Description:

Simulates real user searches on Amazon storefronts to retrieve real-time keyword ranking and search results page data for product research, ASIN position checks, competitor discovery, price comparison, sponsored product analysis, and new product monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to inspect current Amazon search results across supported marketplaces, including ranking positions, prices, ratings, sponsored flags, and delivery-related fields. Agents can use it to plan API calls, summarize SERP data, and guide users through authentication or billing issues when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and may handle generated keys during onboarding.

Mitigation: Treat API keys, shell-profile exports, saved JSON responses, and local cache files as sensitive; review or delete local linkfox output directories after use.

Risk: The onboarding workflow can involve phone/SMS registration and billing or payment order flows.

Mitigation: Use script-driven registration or payment only when the user intentionally wants the agent involved in account setup or purchasing.

Risk: Search calls consume LinkFox credits and repeated exploratory queries can increase cost.

Mitigation: Explain expected credit use before high-frequency calls, reuse the 24-hour cache for identical parameters, and ask before retrying with changed keywords, pages, or delivery locations.

Risk: The security verdict is suspicious because the skill combines credentials, billing actions, automatic feedback reporting, and durable local storage.

Mitigation: Install only after reviewing these behaviors and confirming that LinkFox service access, feedback reporting, and local persistence are acceptable for the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-search)
- [亚马逊前端搜索模拟 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox agent portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are cached for 24 hours by parameter set; full API responses are written under a local linkfox output directory, with stdout showing either full JSON for small responses or a concise summary for large responses.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
