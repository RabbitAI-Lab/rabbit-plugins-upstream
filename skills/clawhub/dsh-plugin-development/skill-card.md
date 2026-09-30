## Description:

Guides developers through creating, debugging, packaging, and publishing DSH/Cordis plugins with templates, API references, and version checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, implement, troubleshoot, and distribute DSH/Cordis plugins. It provides starter templates and checks guidance against the installed DSH version before coding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source-sync scripts or copied examples may run code or fetch external packages.

Mitigation: Review commands and dependencies before execution, and pin external package versions.

Risk: External integrations may access credentials or persistent memory.

Mitigation: Use dedicated, low-scope credentials and review any persistent-memory changes.

Risk: Pre-stable DSH APIs may change and make example plugins incompatible.

Mitigation: Run the version gate against the target DSH checkout and test the generated plugin before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [Project homepage (declared in skill metadata; import provenance unavailable)](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Version gate](references/00-version-gate.md)
- [Plugin templates](references/02-templates.md)
- [API cookbook](references/03-api-cookbook.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated plugin files or bundles may require local testing and version checks before deployment.]

## Skill Version(s):

1.3.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
