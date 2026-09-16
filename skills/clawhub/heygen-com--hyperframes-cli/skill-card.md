## Description:

Guides agents through the HyperFrames CLI workflow for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, and related video-production commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate HyperFrames CLI workflows for video composition setup, validation, preview, local or cloud rendering, publishing, troubleshooting, and asset-related helper commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill normalizes running an external CLI package with npx, which can execute code from package maintainers.

Mitigation: Install only when the HyperFrames npm package and maintainers are trusted, and prefer a pinned or local CLI for controlled environments.

Risk: Telemetry and feedback workflows can submit usage or issue details outside the local environment.

Mitigation: Disable telemetry and feedback unless explicitly wanted, and redact paths, secrets, credentials, and project-identifying details before any report.

Risk: Cloud rendering paths use credentials and may change persistent agent or cloud state.

Mitigation: Review any project wrapper before use, avoid broad confirmation flags such as --yes or --no-confirm casually, and use narrowly scoped cloud credentials.

## Reference(s):

- [HyperFrames CLI Skill](SKILL.md)
- [init, capture, skills](references/init-and-scaffold.md)
- [lint, check, snapshot](references/lint-validate-inspect.md)
- [preview, play, render, publish](references/preview-render.md)
- [cloud - HeyGen-hosted rendering](references/cloud.md)
- [Lambda rendering on AWS](references/lambda.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [doctor, browser](references/doctor-browser.md)
- [Generate a project beat grid](references/beats.md)
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI repository](https://github.com/heygen-com/heygen-cli)
- [HeyGen API](https://api.heygen.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to generate or modify project files and run local, hosted, AWS Lambda, or Google Cloud Run render workflows.]

## Skill Version(s):

1.0.39 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
