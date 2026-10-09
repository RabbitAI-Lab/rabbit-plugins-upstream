## Description:

Guides agents through developing, validating, previewing, rendering, and publishing HyperFrames video projects with the CLI, including local and cloud workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to scaffold and edit HyperFrames projects, check and preview results, troubleshoot failures, and render videos locally or through HeyGen, AWS Lambda, or Google Cloud Run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI commands and project-supplied tools may execute code with the agent's permissions.

Mitigation: Use a project-local locked wrapper or pinned package version; avoid project-local FFmpeg and FFprobe binaries in untrusted projects.

Risk: Cloud rendering, publishing, and infrastructure changes may upload content, incur costs, or delete resources.

Mitigation: Require explicit user approval before cloud rendering, publishing, render deletion, or AWS/GCP deploy and destroy actions.

Risk: Feedback submissions may expose project or user details to an external channel.

Mitigation: Obtain approval before submitting feedback, omit identifying details, and honor telemetry opt-outs.

## Reference(s):

- [HyperFrames CLI skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [CLI development and scaffolding](artifact/references/init-and-scaffold.md)
- [Preview, rendering, publishing, and feedback](artifact/references/preview-render.md)
- [HeyGen-hosted rendering](artifact/references/cloud.md)
- [AWS Lambda rendering](artifact/references/lambda.md)
- [Google Cloud Run rendering](artifact/references/cloudrun.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI commands and project-edit guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of project files and rendered video through CLI commands.]

## Skill Version(s):

1.0.61 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
