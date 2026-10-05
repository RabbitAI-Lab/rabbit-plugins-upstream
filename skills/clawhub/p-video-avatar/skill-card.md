## Description:

Guides an agent in creating a single lip-synced talking-head video from a portrait and a script or narration using Pruna's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through preparing a portrait, confirming a script or narration, and requesting one speaking-avatar clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime installation of unpinned external skills can expand agent behavior beyond the reviewed release.

Mitigation: Review and pin or preinstall dependencies; avoid automatically running install commands in sensitive environments.

Risk: Portraits, scripts, and optional narration or voice data are sent to Pruna's API.

Mitigation: Confirm the data and intended use with the user before uploading or making a paid request.

## Reference(s):

- [p-video-avatar on ClawHub](https://clawhub.ai/pruna-ai/skills/p-video-avatar)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one avatar-video request per invocation; requires a Pruna API key and user-confirmed inputs.]

## Skill Version(s):

1.0.14 (source: ClawHub release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
