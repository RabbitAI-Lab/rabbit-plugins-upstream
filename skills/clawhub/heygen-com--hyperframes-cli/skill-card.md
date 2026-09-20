## Description:

Guides agents through HyperFrames CLI workflows for scaffolding, validating, previewing, rendering, publishing, cloud deployment, diagnostics, and related media utilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to operate HyperFrames CLI workflows for building, checking, previewing, rendering, comparing, publishing, and troubleshooting video compositions across local, HeyGen-hosted, AWS Lambda, and Google Cloud Run paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to run an unpinned npm CLI, so behavior can change through the package or its update path.

Mitigation: Install only when the HyperFrames npm package and publisher update path are trusted; prefer a project wrapper or pinned CLI version for repeatable workflows.

Risk: Some workflows can upload or publish projects, install skills, download browser assets, or manage cloud infrastructure.

Mitigation: Require explicit user approval before cloud, publish, feedback, lambda, cloudrun, browser-download, or skills-install commands; use dry-run and status commands where available.

Risk: Telemetry or feedback commands may send reports outside the local workspace.

Mitigation: Opt out of telemetry or feedback when reports are not desired, and redact secrets, credentials, absolute paths, and sensitive project details before submitting feedback.

## Reference(s):

- [HyperFrames CLI Skill Definition](artifact/SKILL.md)
- [init, capture, skills](artifact/references/init-and-scaffold.md)
- [lint, check, snapshot](artifact/references/lint-validate-inspect.md)
- [preview, play, render, publish](artifact/references/preview-render.md)
- [cloud - HeyGen-hosted rendering](artifact/references/cloud.md)
- [Lambda rendering on AWS](artifact/references/lambda.md)
- [Cloud Run rendering on Google Cloud](artifact/references/cloudrun.md)
- [Compare and batch rendering](artifact/references/compare-and-batch.md)
- [doctor, browser](artifact/references/doctor-browser.md)
- [info, upgrade, compositions, timeline, docs, benchmark, telemetry, asset preprocessing](artifact/references/upgrade-info-misc.md)
- [Generate a project beat grid](artifact/references/beats.md)
- [HeyGen CLI GitHub Repository](https://github.com/heygen-com/heygen-cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, configuration snippets, and file-editing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance may propose commands that execute local, hosted, or cloud infrastructure workflows; review before running.]

## Skill Version(s):

1.0.45 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
