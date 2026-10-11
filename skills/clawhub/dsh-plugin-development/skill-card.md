## Description:

Guides developers through building, debugging, packaging, and publishing DSH (DeepSeek Harness) / Cordis plugins with templates and version checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, troubleshoot, and package DSH plugins, including tools, commands, services, UI slots, and HTTP routes. It helps check plugin guidance against the target DSH version before coding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DSH changes may make plugin examples or API guidance outdated.

Mitigation: Confirm the target DSH version and run local version checks against its source before using examples.

Risk: Generated plugins may expose API keys to subprocesses or introduce third-party packages.

Mitigation: Review generated code, credential handling, and dependencies before installing plugins into a profile.

Risk: Local verification may require cloning DSH source.

Mitigation: Confirm with the developer before cloning or running local verification scripts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [Project homepage (skill metadata)](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Version gate](artifact/references/00-version-gate.md)
- [Plugin templates](artifact/references/02-templates.md)
- [Known plugin pitfalls](artifact/references/05-pitfalls.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated plugin code and configuration require review before installation.]

## Skill Version(s):

1.4.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
