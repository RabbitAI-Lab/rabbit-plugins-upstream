## Description:

Helps developers use the HyperFrames CLI to scaffold, inspect, edit, preview, render, publish, and troubleshoot video projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and manage HyperFrames video projects, inspect timelines and frames, run checks, and preview or render finished videos locally or through cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports unsolicited external feedback and telemetry. The skill documentation says its usage beacon runs at startup and may be account-linked when signed in.

Mitigation: Avoid installing until feedback and telemetry are removed or made opt-in; if using it, review the telemetry opt-out before running the skill.

Risk: ClawScan reports many unpinned CLI commands, which can make the executed CLI version vary.

Mitigation: Pin the HyperFrames CLI version and review it before running commands.

Risk: The security scan is partial and reports some capabilities beyond the stated project workflow.

Mitigation: Review the skill and scan findings before installation; treat the suspicious verdict as a risk signal rather than proof of malicious intent.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames CLI skill instructions](SKILL.md)
- [Scaffolding and capture](references/init-and-scaffold.md)
- [Lint, checks, and snapshots](references/lint-validate-inspect.md)
- [Preview, render, and publish](references/preview-render.md)
- [Cloud rendering](references/cloud.md)
- [AWS Lambda and Google Cloud Run](references/lambda.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and project-editing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and examples depend on the user's project and chosen render target.]

## Skill Version(s):

1.0.87 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
