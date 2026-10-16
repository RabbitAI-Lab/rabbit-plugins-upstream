## Description:

Guides developers through building, checking, previewing, rendering, and publishing HyperFrames video projects with the CLI, locally or through managed and self-hosted cloud services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to scaffold HyperFrames projects, diagnose build and render issues, inspect previews, and produce local or cloud-rendered videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm CLI may execute code that differs from the reviewed release.

Mitigation: Prefer a pinned project wrapper or a locally locked dependency, and review commands before execution.

Risk: Cloud publishing and rendering can upload project content or use account credentials.

Mitigation: Require explicit approval before publishing, uploading, or using cloud credentials.

Risk: Feedback submissions may disclose project details publicly, and infrastructure commands can destroy AWS or GCP resources.

Mitigation: Obtain explicit approval before feedback submission or destructive cloud commands; redact private details and disable telemetry if desired.

## Reference(s):

- [HyperFrames CLI release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview, render, and publish guide](references/preview-render.md)
- [Managed cloud rendering guide](references/cloud.md)
- [AWS Lambda rendering guide](references/lambda.md)
- [Google Cloud Run rendering guide](references/cloudrun.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of project files and rendered videos.]

## Skill Version(s):

1.0.70 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
