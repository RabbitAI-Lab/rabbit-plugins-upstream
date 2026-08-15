## Description:

Queries Jiimore-powered Amazon niche review data from a keyword and helps agents summarize consumer sentiment, customer pain points, and positive or negative review themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and market researchers use this skill to inspect niche-level review topics, sentiment, and customer pain points for Amazon marketplace keywords.

### Deployment Geography for Use:

Global; marketplace data queries are limited to the United States, Japan, and Germany.

## Known Risks and Mitigations:

Risk: The skill uses a paid LinkFox integration and each niche review lookup consumes credits.

Mitigation: Confirm the user understands the credit cost before repeated or exploratory calls, and rely on the built-in cache for identical requests within the same 24-hour window.

Risk: Authentication and onboarding flows may ask for phone/SMS login, generate API keys, and create payment orders.

Mitigation: Prefer self-service account setup, avoid sharing one-time codes in chat when possible, and store API keys in a secret manager instead of plain shell profiles.

Risk: The lookup script writes full API responses to local session files.

Mitigation: Review saved JSON files before sharing them and remove local response files when they contain sensitive business or account information.

Risk: Endpoint override environment variables can change where credentials and request data are sent.

Mitigation: Do not set LinkFox endpoint override variables unless the destination is fully trusted and intentionally configured.

Risk: The skill can send feedback to a separate LinkFox feedback endpoint.

Mitigation: Keep feedback content minimal and avoid including secrets, personal data, or confidential marketplace research.

## Reference(s):

- [Jiimore Amazon Niche Review API Reference](artifact/references/api.md)
- [Authentication and Credits Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-review-from-keyword)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables with saved JSON response files and inline shell commands when setup or billing actions are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script caches matching requests for 24 hours, saves full responses locally, prints small responses inline, and summarizes larger responses unless full inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
