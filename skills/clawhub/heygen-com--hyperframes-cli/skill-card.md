## Description:

Helps agents scaffold, validate, inspect, edit, preview, render, publish, and troubleshoot HyperFrames video projects through the HyperFrames CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production teams use this skill to create and manage HyperFrames projects, edit timelines, preview and render video locally or in hosted cloud environments, and publish finished projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider-account usage checks may access credentials or consume account resources.

Mitigation: Require explicit approval before account-usage checks and prefer a reviewed, pinned CLI wrapper.

Risk: The skill may submit public feedback without a separate approval step.

Mitigation: Require approval before feedback submission or disable feedback with HYPERFRAMES_NO_TELEMETRY=1.

Risk: Project scaffolding may install additional skills.

Mitigation: Set HYPERFRAMES_SKIP_SKILLS=1 when additional skill installation is not wanted.

Risk: Cloud workflows may upload project content, incur charges, or delete infrastructure.

Mitigation: Review and explicitly approve cloud uploads, charges, and infrastructure deletion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames CLI repository (documentation reference)](https://github.com/heygen-com/heygen-cli)
- [Cloud rendering and authentication guidance](artifact/references/cloud.md)
- [Preview, rendering, and publishing guidance](artifact/references/preview-render.md)
- [Feedback and telemetry guidance](artifact/references/feedback.md)
- [Project scaffolding guidance](artifact/references/init-and-scaffold.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and JSON examples; CLI-generated project and video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update project files and render or publish video outputs.]

## Skill Version(s):

1.0.72 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
