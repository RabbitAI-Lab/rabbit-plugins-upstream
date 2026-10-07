## Description:

Guides agents through developing, checking, previewing, and rendering HyperFrames video projects locally or through hosted and self-managed cloud services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to scaffold, inspect, test, preview, render, and publish HyperFrames compositions, including cloud rendering workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feedback reports may be posted to a public channel, and render telemetry is opt-out.

Mitigation: Disable telemetry or require approval before each report; review and redact feedback payloads before submission.

Risk: Cloud upload, publishing, and infrastructure deletion can expose project content or remove cloud resources.

Mitigation: Require explicit confirmation before upload, publish, cloud delete, lambda destroy, or cloudrun destroy; inspect project archives and visibility first.

Risk: Unpinned CLI invocations and skill-pack installations can introduce unexpected changes.

Mitigation: Pin or wrap the CLI version when possible, and confirm skill-pack installations before running them.

## Reference(s):

- [HyperFrames CLI skill](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Project setup and scaffolding](references/init-and-scaffold.md)
- [Linting and validation](references/lint-validate-inspect.md)
- [Preview, rendering, publishing, and feedback](references/preview-render.md)
- [HeyGen-hosted rendering](references/cloud.md)
- [AWS Lambda rendering](references/lambda.md)
- [Google Cloud Run rendering](references/cloudrun.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command examples and project code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of video projects and rendered media.]

## Skill Version(s):

1.0.59 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
