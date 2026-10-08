## Description:

Guides agents through developing, checking, previewing, and rendering video projects with the HyperFrames CLI across local and supported cloud workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to guide video project setup, editing, validation, previews, and approved local or cloud renders with HyperFrames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime CLI commands may use an unpinned npm version.

Mitigation: Prefer a project wrapper or pinned local HyperFrames version before execution.

Risk: Feedback or diagnostics may be sent publicly by default.

Mitigation: Disable telemetry or feedback before sensitive work and require explicit approval before sending feedback.

Risk: Publishing, cloud renders, remote deployments, browser-profile actions, or project uploads may expose project data or incur costs.

Mitigation: Require explicit approval before publishing, cloud rendering, Lambda or Cloud Run deployment, browser-profile actions, or project uploads.

## Reference(s):

- [HyperFrames CLI skill on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview and render workflows](artifact/references/preview-render.md)
- [Validation and inspection workflows](artifact/references/lint-validate-inspect.md)
- [Cloud rendering workflows](artifact/references/cloud.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for agent workflows; rendered video is produced by the CLI, not by the skill itself.]

## Skill Version(s):

1.0.60 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
