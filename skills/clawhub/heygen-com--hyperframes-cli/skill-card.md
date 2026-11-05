## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to build, inspect, edit, preview, render, and publish HyperFrames video projects through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls for telemetry and public feedback, checks AI-provider credentials, and describes paid-plan final renders that upload projects to the cloud by default.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 before first use to opt out; make feedback and quota checks optional; require approval before project uploads or cloud spending.

Risk: The external CLI and some companion documentation were not verified, and claims about redaction and credential handling remain unconfirmed.

Mitigation: Use a reviewed, pinned CLI with narrowly scoped cloud credentials, and verify data handling before sending sensitive project content.

## Reference(s):

- [Scaffold and capture](references/init-and-scaffold.md)
- [Lint, checks, and snapshots](references/lint-validate-inspect.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [Audio beats](references/beats.md)
- [Preview, render, and publish](references/preview-render.md)
- [Browser setup and diagnostics](references/doctor-browser.md)
- [Authentication and cloud rendering](references/cloud.md)
- [AWS Lambda and GCP Cloud Run rendering](references/lambda.md)
- [Google Cloud Run rendering](references/cloudrun.md)
- [CLI conventions](references/conventions.md)
- [CLI updates, project information, and telemetry](references/upgrade-info-misc.md)
- [Feedback](references/feedback.md)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration, Video files]

**Output Format:** [Markdown guidance with shell commands and JSON examples; HyperFrames project files and rendered video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the project, media, and selected local or cloud render target.]

## Skill Version(s):

1.0.84 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
