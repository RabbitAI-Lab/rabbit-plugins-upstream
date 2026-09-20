## Description:

Use when someone wants a simple short clip from text or images, including quick B-roll, drafts, or start/end frame animation, but not when the brief needs cinematic generation, highest quality, tight lip-sync, or imported audio at 1080p.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare and submit one simple Pruna p-video generation request from text, images, optional frame anchors, or short approved audio. It helps route away from cinematic, multi-scene, avatar, motion-transfer, or 1080p/imported-audio requests that require a different Pruna skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install multiple unpinned external Pruna skills.

Mitigation: Use pinned or preapproved prerequisite skill versions, and avoid installing the full Pruna suite unless the broader suite is explicitly needed.

Risk: Prompts, images, or audio may be sent to Pruna's hosted API for third-party processing.

Mitigation: Submit only content approved for third-party processing and confirm environment policy before uploading user media or generated audio.

## Reference(s):

- [ClawHub p-video skill page](https://clawhub.ai/pruna-ai/skills/p-video)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna prediction API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one p-video prediction per invocation and may include upload, prediction, polling, and download guidance.]

## Skill Version(s):

1.0.13 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
