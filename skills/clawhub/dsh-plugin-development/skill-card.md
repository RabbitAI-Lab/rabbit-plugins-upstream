## Description:

Guides developers through building, debugging, packaging, and publishing DSH/Cordis plugins with templates, API references, and version checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to create and troubleshoot DSH/Cordis plugins, including tools, commands, services, UI extensions, HTTP routes, and distributable bundles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The source-sync helper can download upstream DSH code.

Mitigation: Review the helper script and its source destination before running it.

Risk: Generated plugins may invoke external commands or expose HTTP routes and timers.

Mitigation: Review generated code and permissions, and test external integrations and routes before deployment.

Risk: Pre-stable DSH releases can change plugin interfaces.

Mitigation: Run the documented version gate against the intended DSH checkout before using the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [Project homepage](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Version gate](references/00-version-gate.md)
- [Plugin templates](references/02-templates.md)
- [API cookbook](references/03-api-cookbook.md)
- [Plugin workflow](references/06-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance and plugin source or configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes templates and version-checking guidance.]

## Skill Version(s):

1.3.4 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
