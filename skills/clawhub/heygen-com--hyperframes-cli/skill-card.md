## Description:

Guides agents through the HyperFrames CLI workflow for creating, checking, previewing, rendering, publishing, and troubleshooting video compositions across local, HeyGen cloud, AWS Lambda, and Google Cloud Run environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to scaffold HyperFrames projects, run quality checks, preview and render videos, and choose the appropriate local or cloud rendering path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead agents to run mutable `npx hyperframes` commands against private projects or credentialed environments.

Mitigation: Review the skill before installation, prefer a pinned or project-local HyperFrames CLI, and require approval before executing commands with project or credential access.

Risk: Feedback, publish, cloud render, cloud delete, Lambda, Cloud Run, and skill-install commands can affect external services or expose project details.

Mitigation: Require explicit user approval before those commands and confirm the target project, account, and visibility settings.

Risk: Feedback diagnostics are submitted publicly and may contain paths, identifiers, logs, or other sensitive context.

Mitigation: Review and redact the exact payload, diagnostics, credentials, and private project details before sending feedback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI GitHub repository](https://github.com/heygen-com/heygen-cli)
- [Generate a project beat grid](artifact/references/beats.md)
- [cloud - HeyGen-hosted rendering](artifact/references/cloud.md)
- [Cloud Run rendering on Google Cloud](artifact/references/cloudrun.md)
- [Compare and batch rendering](artifact/references/compare-and-batch.md)
- [doctor, browser](artifact/references/doctor-browser.md)
- [init, capture, skills](artifact/references/init-and-scaffold.md)
- [Lambda rendering on AWS](artifact/references/lambda.md)
- [lint, check, snapshot](artifact/references/lint-validate-inspect.md)
- [preview, play, render, publish](artifact/references/preview-render.md)
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](artifact/references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.40 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
