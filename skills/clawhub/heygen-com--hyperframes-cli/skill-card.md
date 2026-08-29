## Description:

Guides agents through HyperFrames CLI workflows for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, telemetry, media utilities, and related failure investigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production agents use this skill to run the HyperFrames CLI development loop, validate compositions, preview timelines, render locally or in cloud environments, and diagnose build or render failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to run broad local, network, rendering, and cloud actions through the HyperFrames CLI.

Mitigation: Install it only for environments where HyperFrames CLI workflows are expected, and require review before capture, publish, cloud, Lambda, or Cloud Run commands are executed.

Risk: Telemetry and feedback commands may send workflow information outside the local environment.

Mitigation: Review telemetry and feedback defaults before use, and set HYPERFRAMES_NO_TELEMETRY=1 where stricter control is required.

Risk: Cloud rendering, publish, and issue-reporting workflows may upload project archives or reproduction material.

Mitigation: Avoid these commands on sensitive projects without explicit approval, inspect archives with dry-run workflows when available, and redact private paths or identifiers from feedback.

Risk: Hosted rendering and authentication workflows may use HeyGen or HyperFrames API credentials.

Mitigation: Use scoped credentials, prefer environment-specific secrets handling, and disable skill loading with HYPERFRAMES_SKIP_SKILLS=1 where the environment requires stricter control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames CLI workflow](SKILL.md)
- [Generate a project beat grid](references/beats.md)
- [HeyGen-hosted cloud rendering](references/cloud.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [Doctor and browser](references/doctor-browser.md)
- [Init, capture, and skills](references/init-and-scaffold.md)
- [Lambda rendering on AWS](references/lambda.md)
- [Lint, check, and snapshot](references/lint-validate-inspect.md)
- [Preview, play, render, and publish](references/preview-render.md)
- [Info, upgrade, compositions, docs, benchmark, telemetry, and asset preprocessing](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline shell commands and command contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create project files, render media, snapshots, public previews, feedback reports, and cloud rendering jobs through the HyperFrames CLI.]

## Skill Version(s):

1.0.31 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
