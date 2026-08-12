## Description:

Searches the live web and returns extracted result content that agents can summarize with source titles and URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill when an agent needs current web information, recent news, community discussion, product research, or fact checking beyond its local context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and LinkFox account data may be sent to LinkFox services.

Mitigation: Avoid sensitive personal or business information in queries and use the skill only when LinkFox service processing is acceptable.

Risk: The skill includes paid-plan ordering and payment QR generation.

Mitigation: Prefer self-service API-key setup where possible and verify any plan, payment URL, or payment QR before proceeding.

Risk: Search responses and session metadata may be stored locally.

Mitigation: Review local output paths and remove stored results when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tsearch-search)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with source titles and URLs; JSON or brief text summaries from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search requests use a single keyword string up to 1000 characters; large responses may be written locally and summarized.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
