## Description:

Guides agents in editing an existing short video from a text instruction, with optional reference images for targeted changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request focused edits to an existing video, such as changing colors, objects, text, lighting, or surroundings while preserving the rest of the clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source videos, optional reference images, and edit prompts are sent to Pruna's service using an API key.

Mitigation: Only submit media and prompts you are comfortable sharing with Pruna, and protect the API key.

Risk: Companion skills may be installed through commands that fetch dependencies.

Mitigation: Review or pin companion skill install commands when stable, auditable dependencies are required.

## Reference(s):

- [p-video-edit on ClawHub](https://clawhub.ai/pruna-ai/skills/p-video-edit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides submission of a source video of up to 15 seconds and optional reference images; the service returns an edited video.]

## Skill Version(s):

1.0.14 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
