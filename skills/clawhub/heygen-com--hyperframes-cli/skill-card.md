## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create, inspect, validate, edit, preview, render, and publish HyperFrames video projects from the CLI, including local and cloud workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send public feedback reports automatically.

Mitigation: Disable public feedback with the documented telemetry opt-out or require approval for each report.

Risk: Usage checks may access AI-provider credentials.

Mitigation: Override automatic account-usage checks unless access to those credentials is authorized.

Risk: Cloud workflows may upload project files or change cloud infrastructure.

Mitigation: Approve uploads and infrastructure changes for a specific project.

Risk: The external CLI's credential handling and reporting implementation is unverified.

Mitigation: Prefer a reviewed, locked CLI version and use --skip-skills to avoid installing additional skills.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview and render](references/preview-render.md)
- [Cloud rendering](references/cloud.md)
- [AWS Lambda rendering](references/lambda.md)
- [Google Cloud Run rendering](references/cloudrun.md)
- [Lint, check, and inspect](references/lint-validate-inspect.md)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command suggestions and workflow guidance for a HyperFrames project.]

## Skill Version(s):

1.0.78 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
