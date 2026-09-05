## Description:

Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-generation operators use this skill to prepare Pruna API calls that swap a person, outfit, or product in an existing video while preserving camera movement, audio, and unmentioned scene elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install related Pruna skills from unpinned references.

Mitigation: Review or pin prerequisite skill sources before installation.

Risk: Source videos and reference images may contain sensitive identity media and are uploaded to Pruna's API.

Mitigation: Avoid sensitive or non-consensual media and confirm that upload handling is acceptable before use.

Risk: The optional disable_safety_checker parameter can reduce safety controls.

Mitigation: Leave safety checking enabled unless a reviewer has explicitly accepted the implications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-replace)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands and API request configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-provided source video plus one to four reference images.]

## Skill Version(s):

1.0.11 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
