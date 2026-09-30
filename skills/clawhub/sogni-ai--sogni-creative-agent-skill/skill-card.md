## Description:

Helps agents create and edit images, videos, music, and other media through Sogni AI's creative tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators, developers, and their agents use this skill to generate and edit visual, audio, and video content, manage reusable personas, and coordinate multi-step creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI accesses the user's Sogni API key and may store credentials and preferences between sessions.

Mitigation: Provide the key only in a trusted environment, restrict access to stored credentials, and review retained data.

Risk: Hosted generation uploads selected media to Sogni and can incur provider or token charges.

Mitigation: Review media before using hosted modes, use direct or local modes where uploads are inappropriate, and set cost limits where available.

Risk: Package installation and self-update can change the code the agent runs.

Mitigation: Pin package versions in controlled environments and review changes before updating.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Hosted API guide](artifact/references/hosted-api.md)
- [Model reference](artifact/references/models.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Media files]

**Output Format:** [Markdown instructions and command output, optionally with generated media files or links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Machine-readable JSON results are available for agent workflows.]

## Skill Version(s):

3.54.3 (source: release metadata, SKILL.md metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
