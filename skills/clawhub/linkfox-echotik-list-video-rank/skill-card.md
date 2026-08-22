## Description:

Queries EchoTik TikTok Shop video rankings by day, week, or month across supported marketplaces and ranking metrics, returning ranked video, creator, engagement, sales, and estimated GMV data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers, marketers, and analysts use this skill to find top TikTok Shop videos for a selected date range, region, and ranking metric. It helps compare popularity and selling performance while preserving the API's ranked order and estimation notices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox services receive ranking queries and possible feedback content.

Mitigation: Review query and feedback content before use, and avoid sending confidential business or personal data unless the user accepts LinkFox handling it.

Risk: The auth and billing flow can collect phone/SMS login information and create payment orders.

Mitigation: Prefer self-service account setup through LinkFox, require explicit user consent before login or payment actions, and do not retain codes, API keys, or payment details in chat.

Risk: Generated API keys, saved responses, and cache files may contain sensitive data.

Mitigation: Treat API keys and saved JSON files as sensitive, restrict workspace access, and delete response or cache files when they are no longer needed.

Risk: Custom LINKFOX_* API URL variables can redirect requests to non-default endpoints.

Mitigation: Use default LinkFox endpoints unless a trusted administrator has intentionally configured alternate URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-video-rank)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, JSON API responses, saved JSON files, and shell commands for invocation or account setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes complete responses under the current workspace, prints full JSON for small responses or summaries for larger responses, supports optional inline output, and uses a 24-hour local cache by default.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
