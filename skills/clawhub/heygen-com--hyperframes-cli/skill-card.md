## Description:

Use the HyperFrames CLI development loop for scaffolding, checking, previewing, rendering, publishing, diagnosing, and managing local, HeyGen-hosted cloud, AWS Lambda, and Google Cloud Run video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to operate HyperFrames CLI workflows for video composition projects, including project setup, validation, preview, rendering, cloud deployment choices, diagnostics, and feedback reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to run mutable npm CLI code.

Mitigation: Install only from a trusted HyperFrames package source and prefer a project-local pinned wrapper or exact package version.

Risk: The skill can alter local agent instruction packs through external skill checks or installs.

Mitigation: Set HYPERFRAMES_SKIP_SKILLS=1 when external agent skills should not be checked or installed.

Risk: Feedback and telemetry may submit environment metadata or public feedback payloads.

Mitigation: Disable telemetry when metadata should not be sent and review feedback payloads before public submission.

Risk: Cloud, AWS, and GCP commands may upload or modify project assets and infrastructure.

Mitigation: Use only scoped credentials and projects that are approved for upload, rendering, or infrastructure changes.

## Reference(s):

- [HyperFrames CLI Skill](SKILL.md)
- [Generate a Project Beat Grid](references/beats.md)
- [Cloud: HeyGen-hosted Rendering](references/cloud.md)
- [Cloud Run Rendering on Google Cloud](references/cloudrun.md)
- [Compare and Batch Rendering](references/compare-and-batch.md)
- [Doctor and Browser](references/doctor-browser.md)
- [Init, Capture, and Skills](references/init-and-scaffold.md)
- [Lambda Rendering on AWS](references/lambda.md)
- [Lint, Check, and Snapshot](references/lint-validate-inspect.md)
- [Preview, Play, Render, and Publish](references/preview-render.md)
- [Info, Upgrade, Compositions, Docs, Benchmark, Telemetry, and Asset Preprocessing](references/upgrade-info-misc.md)
- [HeyGen CLI Repository](https://github.com/heygen-com/heygen-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to create, inspect, upload, render, and verify local or cloud video project artifacts.]

## Skill Version(s):

1.0.36 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
