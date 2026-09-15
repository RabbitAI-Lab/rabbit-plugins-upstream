## Description:

Guides agents through HyperFrames CLI workflows for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, media preprocessing, telemetry, and upgrades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and production-focused agents use this skill to operate the HyperFrames CLI development loop for video composition, validation, preview, rendering, publishing, and cloud execution. It also supports diagnosing build and render failures across local, HeyGen-hosted, AWS Lambda, and Google Cloud Run paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on unpinned `npx hyperframes` execution, which can run package code from the npm provider at execution time.

Mitigation: Install only when the HyperFrames npm package and provider are trusted, and prefer a pinned or project-local CLI for repeatable production workflows.

Risk: Feedback and issue-reporting workflows can send diagnostics or reproduction details to a public channel.

Mitigation: Review or opt out of feedback before submission, and redact paths, project names, secrets, and credentials from any report.

Risk: Cloud, AWS Lambda, and Google Cloud Run workflows use external services and privileged credentials that can incur cost or modify cloud infrastructure.

Mitigation: Use dedicated least-privilege credentials, confirm billing and target project/account, and run dry-run or policy validation paths before deployment or rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI GitHub repository](https://github.com/heygen-com/heygen-cli)
- [cloud - HeyGen-hosted rendering](references/cloud.md)
- [preview, play, render, publish](references/preview-render.md)
- [lint, check, snapshot](references/lint-validate-inspect.md)
- [Lambda rendering on AWS](references/lambda.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [doctor, browser](references/doctor-browser.md)
- [init, capture, skills](references/init-and-scaffold.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [Generate a project beat grid](references/beats.md)
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to run local CLI commands, start preview servers, render media files, publish projects, or use credentialed cloud workflows after user approval.]

## Skill Version(s):

1.0.38 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
