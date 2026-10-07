## Description:

Helps an agent plan, execute, verify, and export video edits from natural-language requests through Levea's video-editing service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and editors use this skill to request video edits such as captions, short clips, reframing, audio cleanup, and exports through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project identifiers, scene data, images, asset descriptors, and approval-state memory are sent to the configured Levea API.

Mitigation: Review the provider's data-handling terms before using sensitive media or project data.

Risk: Edits to user content can be destructive or irreversible, and beta outputs can be wrong.

Mitigation: Describe the planned edit and obtain explicit confirmation; require plan approval for destructive or irreversible work.

## Reference(s):

- [Levea AI Video Editor on ClawHub](https://clawhub.ai/brajendrak00068/skills/levea-ai-video-editor)
- [Skill metadata homepage](https://github.com/brajendrak00068/openclaw-ai-video-editor#readme)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown instructions and shell examples for JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes edit plans, approval, verification, and export results.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
