## Description:

Use the HyperFrames CLI development loop for project scaffolding, checking, previewing, rendering, publishing, diagnostics, telemetry, media preprocessing, and local, HeyGen-hosted, AWS Lambda, or Google Cloud Run rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to operate HyperFrames CLI workflows for creating, validating, previewing, rendering, publishing, and diagnosing HTML-based video projects across local and cloud environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud render and publish workflows can upload project archives that may include secrets, customer data, proprietary media, or files that should not leave the local environment.

Mitigation: Run the documented dry-run/archive checks before cloud render or publish, inspect included files, and narrow `.hyperframesignore` rules without excluding required render assets.

Risk: AWS Lambda and Google Cloud Run paths can deploy self-managed cloud infrastructure and consume cloud resources.

Mitigation: Use these paths only when AWS or GCP ownership is explicit, confirm credentials and billing context, and prefer the managed or local render path when infrastructure deployment is not required.

Risk: Anonymous telemetry or feedback reports may be unacceptable for some environments.

Mitigation: Check telemetry posture before use, disable telemetry where required, and avoid feedback reports or public issue publishing unless the user accepts that disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI](https://github.com/heygen-com/heygen-cli)
- [beats.md](references/beats.md)
- [cloud.md](references/cloud.md)
- [cloudrun.md](references/cloudrun.md)
- [compare-and-batch.md](references/compare-and-batch.md)
- [doctor-browser.md](references/doctor-browser.md)
- [init-and-scaffold.md](references/init-and-scaffold.md)
- [lambda.md](references/lambda.md)
- [lint-validate-inspect.md](references/lint-validate-inspect.md)
- [preview-render.md](references/preview-render.md)
- [upgrade-info-misc.md](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Code, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to generate or inspect video project files, JSON command output, rendered media, snapshots, archives, and cloud infrastructure configuration.]

## Skill Version(s):

1.0.30 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
