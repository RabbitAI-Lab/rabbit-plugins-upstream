## Description:

Guides developers through HyperFrames CLI workflows to build, validate, preview, render, and troubleshoot video projects locally or in the cloud.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to manage HyperFrames video projects, check and preview compositions, and render approved outputs locally or with cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feedback commands may submit diagnostics publicly.

Mitigation: Review submitted content and require explicit approval before sending feedback.

Risk: Unpinned npm execution may run unexpected CLI code.

Mitigation: Use a pinned or project-local HyperFrames CLI wrapper rather than bare npx hyperframes.

Risk: Cloud rendering and infrastructure commands may access credentials, incur costs, or remove resources.

Mitigation: Require explicit approval before cloud render, publish, Lambda, Cloud Run, delete, or destroy commands.

## Reference(s):

- [HyperFrames CLI skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview and rendering guide](references/preview-render.md)
- [Cloud rendering guide](references/cloud.md)
- [Validation and inspection guide](references/lint-validate-inspect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of project files and rendered videos after user approval.]

## Skill Version(s):

1.0.53 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
