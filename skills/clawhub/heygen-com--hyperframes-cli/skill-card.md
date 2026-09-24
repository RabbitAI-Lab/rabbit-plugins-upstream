## Description:

Guides agents through the HyperFrames CLI development loop for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, telemetry, and related video-composition workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create, inspect, preview, render, and troubleshoot HyperFrames video compositions across local, HeyGen-hosted, AWS Lambda, and Google Cloud Run workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Floating npx execution can run the currently resolved HyperFrames package rather than a pinned project dependency.

Mitigation: Prefer an existing project wrapper or pinned package version when available, and review commands before execution.

Risk: Cloud render, publish, feedback, and skills-install workflows can upload project files, publish reproductions, send reports, or modify the local coding environment.

Mitigation: Confirm user intent before these commands, use dry-run or preview modes where available, and avoid public issue or publish flags without consent.

Risk: Telemetry and feedback workflows may send usage or troubleshooting reports.

Mitigation: Disable telemetry or feedback when reporting is not desired, and strip absolute paths, user identifiers, and sensitive project details from reproduction packets.

Risk: Cloud rendering requires API credentials and may interact with external HeyGen, AWS, or Google Cloud infrastructure.

Mitigation: Use the documented credential paths or environment variables, avoid exposing secrets in logs, and verify cloud target, cost, and cleanup expectations before rendering.

## Reference(s):

- [HyperFrames CLI Skill](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI](https://github.com/heygen-com/heygen-cli)
- [Generate a project beat grid](references/beats.md)
- [Cloud - HeyGen-hosted rendering](references/cloud.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [Doctor and browser](references/doctor-browser.md)
- [Init, capture, skills](references/init-and-scaffold.md)
- [Lambda rendering on AWS](references/lambda.md)
- [Lint, check, snapshot](references/lint-validate-inspect.md)
- [Preview, play, render, publish](references/preview-render.md)
- [Info, upgrade, compositions, timeline, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented command-output handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local and cloud video workflows; HyperFrames commands may produce rendered media files, snapshots, JSON diagnostics, or hosted preview URLs.]

## Skill Version(s):

1.0.47 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
