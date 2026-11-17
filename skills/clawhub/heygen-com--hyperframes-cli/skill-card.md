## Description:

HyperFrames CLI - scaffold, check frames, edit timelines, preview, render, share and project history; read JSON and recover from failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to operate HyperFrames projects: scaffold and inspect compositions, check and edit timelines, preview and render videos, and manage sharing or project history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud and account actions can affect signed-in services, cloud resources, or billing.

Mitigation: Review each cloud or account-related command and confirm the target account, project, and expected charges before running it.

Risk: The skill starts a usage beacon that may send account-linked telemetry, and its guidance includes feedback reporting.

Mitigation: Review the telemetry opt-out and feedback behavior before use, and avoid sending feedback unless it is intended.

Risk: The security guidance identifies an unpinned CLI dependency.

Mitigation: Review the package and version that will run before installing or executing commands.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames cloud rendering](artifact/references/cloud.md)
- [HyperFrames Lambda rendering](artifact/references/lambda.md)
- [HyperFrames Cloud Run rendering](artifact/references/cloudrun.md)
- [HyperFrames checks and validation](artifact/references/lint-validate-inspect.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with shell command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate on HyperFrames projects; Node.js 22+ and FFmpeg are required.]

## Skill Version(s):

1.0.95 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
