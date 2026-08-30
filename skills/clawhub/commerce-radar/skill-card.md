## Description:

Commerce Radar helps agents search products and price evidence, inspect product details, analyze public stores, and create keyword-based e-commerce competitive reports using COMMERCE_RADAR_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to gather e-commerce product evidence, compare prices, inspect public store information, and generate competitive research reports from keyword queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, store, and keyword queries are sent to the AI Skills Commerce Radar service under the configured API key.

Mitigation: Install and use the skill only when this data sharing is acceptable for the user's workflow.

Risk: The Commerce Radar API key could be exposed through chat, logs, request bodies, or shared files.

Mitigation: Keep COMMERCE_RADAR_API_KEY in environment configuration only and do not ask users to paste the key into conversation.

Risk: Billing information and retry behavior can be misread when asynchronous requests are retried or replayed.

Mitigation: Use idempotency keys correctly, preserve the original request during retries, and rely only on the documented billing headers.

Risk: Returned prices, store summaries, and competitive reports may be partial, time-bound, or dependent on upstream provider availability.

Mitigation: Present returned values as observed evidence, disclose partial or failed task states, and avoid claiming stable prices, complete inventory, or guaranteed real-time data.

## Reference(s):

- [Commerce Radar ClawHub Listing](https://clawhub.ai/youteacher/skills/commerce-radar)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/commerce-radar/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/commerce-radar/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/commerce-radar/HTTP-REQUESTS.md)
- [Behavior and Error Rules](https://ai-skills.open-idea.net/skill-docs/commerce-radar/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown text with optional shell command snippets and structured API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include task IDs, final task statuses, product or store evidence, generated reports, billing header summaries, and guidance for retry or reconciliation.]

## Skill Version(s):

1.2.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
