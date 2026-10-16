## Description:

Creates and edits images, video, music, and speech through Sogni AI, with support for reusable personas and creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to generate and edit visual and audio media, manage reference personas, and run multi-step creative workflows through Sogni AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Sogni API key and can send selected media to Sogni or vendor-backed services.

Mitigation: Protect the API key; review media before submission and use documented direct or local modes for private content.

Risk: Agent registration can persist beyond the current session.

Mitigation: Review and approve any persistent agent-registration step before running it.

Risk: Self-updates or disabling cost confirmation can change behavior or incur unexpected charges.

Mitigation: Require explicit human approval before self-updating or disabling cost confirmation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [Model guide](references/models.md)
- [Hosted API guide](references/hosted-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Media files]

**Output Format:** [Markdown guidance and CLI commands; generated image, video, and audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media is saved to a user-selected or working-directory path; supported commands can return structured JSON.]

## Skill Version(s):

3.56.2 (source: ClawHub release, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
