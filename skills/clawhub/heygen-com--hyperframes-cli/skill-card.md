## Description:

Guides agents through HyperFrames CLI workflows for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, and related media tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to operate the HyperFrames CLI development loop for video composition projects, including local validation, preview, rendering, cloud delivery, troubleshooting, and batch workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud render, publish, feedback with file-issue, AWS Lambda, and Google Cloud Run workflows can upload local project files, which may expose secrets or proprietary assets if the project archive is not reviewed.

Mitigation: Review upload contents before these workflows, use dry-run and narrow ignore rules for cloud archives, and only share or publish files with explicit intent.

Risk: Credentialed cloud commands and telemetry-related commands may use HeyGen or HyperFrames credentials and may send operational metadata.

Mitigation: Store credentials through the documented credential paths or environment variables, disable telemetry when desired, and redact paths, secrets, credentials, and identifying details from feedback.

Risk: AWS Lambda and Google Cloud Run commands can create or modify cloud infrastructure and incur provider costs.

Mitigation: Run infrastructure commands only when those cloud changes are intended, confirm account and region settings first, and clean up provider resources when they are no longer needed.

## Reference(s):

- [HyperFrames CLI Skill](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Generate a project beat grid](references/beats.md)
- [cloud - HeyGen-hosted rendering](references/cloud.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [doctor, browser](references/doctor-browser.md)
- [init, capture, skills](references/init-and-scaffold.md)
- [Lambda rendering on AWS](references/lambda.md)
- [lint, check, snapshot](references/lint-validate-inspect.md)
- [preview, play, render, publish](references/preview-render.md)
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, JSON examples, and configuration notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local, managed cloud, AWS Lambda, and Google Cloud Run execution paths depending on the user's rendering requirements.]

## Skill Version(s):

1.0.28 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
