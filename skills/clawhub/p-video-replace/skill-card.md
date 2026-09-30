## Description:

Guides agents in replacing a person, outfit, or product in existing footage while preserving camera movement and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide reference-image-based replacements in a source video through Pruna's hosted API, while retaining the original scene's camera movement and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source video and reference images are uploaded to Pruna's hosted API.

Mitigation: Use only media approved for third-party upload; avoid confidential or regulated footage unless authorized.

Risk: Replacing identifiable people in video can be done without their consent.

Mitigation: Obtain consent for identifiable people and use only media you are authorized to edit.

Risk: Related skill installation commands may fetch unpinned content.

Mitigation: Prefer pinned or otherwise trusted installer commands for related skills.

## Reference(s):

- [p-video-replace on ClawHub](https://clawhub.ai/pruna-ai/skills/p-video-replace)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with curl examples and video-editing prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for submitting a source video and 1–4 reference images; the hosted service returns the edited video.]

## Skill Version(s):

1.0.14 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
