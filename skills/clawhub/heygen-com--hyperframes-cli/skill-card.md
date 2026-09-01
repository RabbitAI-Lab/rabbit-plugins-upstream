## Description:

Guides agents through HyperFrames CLI workflows for creating, checking, previewing, rendering, publishing, and diagnosing video compositions across local, HeyGen cloud, AWS Lambda, and Google Cloud Run environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to operate HyperFrames projects: scaffold or capture compositions, select catalog moves, run lint/check/snapshot feedback loops, preview for approval, render locally or in cloud, publish, and diagnose environment or render failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some workflows can upload project source and assets or publish a project publicly.

Mitigation: Use local preview and render for routine work, run dry-run checks before cloud uploads, review .hyperframesignore for sensitive files, and require explicit consent before publishing or filing public reproduction projects.

Risk: Cloud rendering can use stored HeyGen credentials or API-key environment variables.

Mitigation: Verify the active credential source before cloud work, avoid exposing credential values in logs or feedback, and clear or opt out of credentials when cloud rendering is not intended.

Risk: AWS Lambda and Google Cloud Run workflows can create cloud infrastructure and incur cost.

Mitigation: Use managed cloud, Lambda, or Cloud Run only when the user explicitly needs that path, validate dry runs and IAM policy expectations first, and clean up retained resources after rendering.

Risk: Telemetry and feedback workflows may send anonymous usage data or public-channel reports.

Mitigation: Opt out of telemetry or feedback when the user does not want reports sent, and redact secrets, absolute paths, and identifying details before submitting feedback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI GitHub repository](https://github.com/heygen-com/heygen-cli)
- [Generate a project beat grid](references/beats.md)
- [HeyGen-hosted rendering](references/cloud.md)
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

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to create or modify project files, preview URLs, rendered media, cloud render jobs, or deployment configuration.]

## Skill Version(s):

1.0.32 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
