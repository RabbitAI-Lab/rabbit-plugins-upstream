## Description:

AI Video Generator helps create videos with Luma Dream Machine, Runway ML, and Kling AI, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaozewen0519](https://clawhub.ai/user/zhaozewen0519)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from prompts or input images through supported third-party video APIs. It is suited for agent-assisted command preparation, API-key configuration, and video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional input images are sent to third-party video generation providers.

Mitigation: Avoid confidential, regulated, or personal content unless the selected provider is approved for that data.

Risk: Video generation depends on user-supplied provider API keys and external service quotas.

Mitigation: Use scoped API keys where available, store them in environment variables, and confirm quota or billing limits before running generation jobs.

Risk: Kling image-input behavior may differ from the local file path workflow described by the artifact.

Mitigation: Verify Kling image-input handling with non-sensitive test files before relying on it for production workflows.

## Reference(s):

- [Ai Video Generator on ClawHub](https://clawhub.ai/zhaozewen0519/skills/ai-video-generator)
- [Luma AI API Documentation](https://docs.lumalabs.ai)
- [Runway API Documentation](https://docs.runwayml.com)
- [Kling AI](https://klingai.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and generated MP4 video files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a supported provider API key; optional image inputs may be sent to the selected provider.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
