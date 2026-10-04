## Description:

Enables agents to create and edit images, videos, music, and speech through Sogni AI, with tools for creative workflows and saved preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to direct an agent to produce or refine images, videos, speech, and music, and to manage multi-step creative projects with Sogni AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses the Sogni API key and persistent Sogni configuration.

Mitigation: Use a dedicated key, protect local credentials, and approve installation only when this access is acceptable.

Risk: Generation requests may upload referenced private images, audio, or video.

Mitigation: Review the media and destination before approving uploads or hosted workflow runs.

Risk: Generation and vendor-model selections can spend paid credits, especially when cost confirmation is disabled.

Mitigation: Require approval for vendor models and --no-confirm-cost, and check the expected cost first.

Risk: Self-update can change the installed skill or CLI.

Mitigation: Require explicit approval before updating and review the new release.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [Model guide](references/models.md)
- [Hosted API guide](references/hosted-api.md)
- [Sogni pricing](https://docs.sogni.ai/pricing/#spark-packs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Media files]

**Output Format:** [Markdown guidance and CLI results with generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return project IDs and status for long-running generations.]

## Skill Version(s):

3.54.4 (source: release metadata, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
