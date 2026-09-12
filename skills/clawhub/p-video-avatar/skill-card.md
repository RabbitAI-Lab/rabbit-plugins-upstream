## Description:

Use when someone wants a person on camera speaking a script - lip-synced host, spokesperson, or narrated avatar from a portrait photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare a single Pruna p-video-avatar prediction that turns a portrait, script or narration audio, and prompt settings into a lip-synced talking-head video clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends portrait images, scripts, and narration audio to Pruna for video generation.

Mitigation: Use it only when the user is comfortable with Pruna processing those inputs and has approved the generation details.

Risk: The skill instructs agents to install multiple external Pruna skills with unpinned npx commands.

Mitigation: Review or pin referenced skill installs before running them, especially in environments with private files, secrets, or persistent agent skill directories.

## Reference(s):

- [p-video-avatar ClawHub release](https://clawhub.ai/pruna-ai/skills/p-video-avatar)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash code blocks and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user confirmation before creating paid predictions.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
