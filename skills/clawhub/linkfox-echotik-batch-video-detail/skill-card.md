## Description:

Batch-fetches detailed analytics for known TikTok video IDs or URLs, including engagement, creator metadata, recent momentum, and estimated sales or GMV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and analysts use this skill to compare known TikTok videos by views, likes, comments, shares, estimated sales or GMV, creator details, and recency metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can consume paid LinkFox credits and create payment orders during onboarding.

Mitigation: Confirm cost expectations before repeated lookups or order creation, and prefer an existing limited API key when available.

Risk: The skill can send TikTok video IDs or URLs and session metadata to LinkFox and store full responses locally.

Mitigation: Use only trusted LinkFox endpoint environment variables and review saved response files before sharing or committing them.

Risk: Onboarding can ask for phone numbers and verification codes to provision API keys.

Mitigation: Use self-service key retrieval where possible, and provide phone or SMS codes only when account setup is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-batch-video-detail)
- [EchoTik batch video detail API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and comparison tables, with JSON response files when the script runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized unless inline output is requested; full responses are stored in a session-scoped LinkFox data directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
