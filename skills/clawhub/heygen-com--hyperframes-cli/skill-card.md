## Description:

Guides agents through using the HyperFrames CLI to scaffold, inspect, edit, preview, render, and publish video projects, and to troubleshoot failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and manage HyperFrames video projects, inspect and edit timelines, check visual output, render locally or in the cloud, and recover from common failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unpinned package commands.

Mitigation: Review package commands before running them and pin versions when reproducibility matters.

Risk: Usage telemetry and feedback commands can send information externally, and telemetry may be account-linked when signed in.

Mitigation: Review the information sent and the CLI's telemetry opt-out settings before invoking these commands.

Risk: Cloud workflows include teardown capability that can remove deployed resources.

Mitigation: Review the target environment and affected resources before running teardown operations.

Risk: The security scan was partial because it could not resolve two local references.

Mitigation: Review the unresolved references and the relevant commands before relying on the scan as a complete assessment.

## Reference(s):

- [HyperFrames CLI release on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview, render, and publish](artifact/references/preview-render.md)
- [Cloud rendering and authentication](artifact/references/cloud.md)
- [Lint, checks, and snapshots](artifact/references/lint-validate-inspect.md)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or modify video project files and rendered media.]

## Skill Version(s):

1.0.86 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
