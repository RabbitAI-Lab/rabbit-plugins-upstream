## Description:

Generate and edit video with InfiniteTalk through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, or transform video with InfiniteTalk through RunAPI, using the CLI for one-off generation and SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, input files, and generated media may be sent to an external provider.

Mitigation: Review data sensitivity, expected retention, and user authorization before using RunAPI for a generation task.

Risk: Video generation can incur provider costs.

Mitigation: Review expected pricing and rate limits before submitting jobs.

Risk: Generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download generated media into durable storage within the stated seven-day window when long-term access is required.

Risk: Saved CLI credentials can persist beyond a single task.

Mitigation: Prefer environment-based API-key authentication for agents and headless runs unless saved CLI credentials are intentional.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-infinitetalk)
- [RunAPI InfiniteTalk Homepage](https://runapi.ai/models/infinitetalk)
- [RunAPI InfiniteTalk Model Overview](https://runapi.ai/models/infinitetalk.md)
- [RunAPI Meigen AI Provider Comparison](https://runapi.ai/providers/meigen-ai.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve external RunAPI service calls that create temporary generated-media URLs.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
