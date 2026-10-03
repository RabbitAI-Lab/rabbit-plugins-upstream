## Description:

Guides agents through creating, checking, previewing, rendering, and publishing HyperFrames video projects with the CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to build and troubleshoot HyperFrames compositions, then preview and render them locally or through hosted and self-managed cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running mutable npm commands can execute code from an untrusted package source.

Mitigation: Review the HyperFrames package source and prefer a pinned version or project-provided CLI wrapper.

Risk: Feedback and telemetry can send information to a public or external destination.

Mitigation: Disable reporting when unsuitable and obtain explicit approval before submitting feedback.

Risk: Publishing, cloud uploads, and AWS or GCP deployment or destruction can expose assets or change cloud resources.

Mitigation: Require explicit approval before uploads, publishing, deployments, or destruction commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview and render guide](references/preview-render.md)
- [Checks and inspection guide](references/lint-validate-inspect.md)
- [Hosted cloud rendering guide](references/cloud.md)
- [AWS Lambda rendering guide](references/lambda.md)
- [Google Cloud Run rendering guide](references/cloudrun.md)
- [HyperFrames catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, CLI commands, and project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project changes and renders should be reviewed before publishing or deployment.]

## Skill Version(s):

1.0.55 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
