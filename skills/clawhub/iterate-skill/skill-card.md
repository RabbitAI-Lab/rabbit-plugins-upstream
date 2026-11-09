## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. v3.0 adds a dual-mode (the original iterate mode plus a defensive-programming mode via /iterate defensive) that performs normal incremental coding tasks with defensive discipline end-to-end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use the skill with an AI coding assistant to review and improve a codebase through repeated multi-dimension review, fixes, and validation, or to complete incremental coding tasks with defensive checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned installer or source update could introduce unexpected changes.

Mitigation: Pin installs and updates to a release, verify its published checksum, and review the source before running it.

Risk: Signing credentials could be exposed or misused.

Mitigation: Keep signing keys out of the project workspace and limit access to the credentials needed for a specific signing operation.

Risk: Network or publishing actions may exceed the intended code-iteration task.

Mitigation: Review the requested action and destination before allowing network access or publishing.

## Reference(s):

- [Project repository](https://github.com/jingzhao-l/iterate-skill)
- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Code changes, Markdown review reports, shell commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested coding or review task.]

## Skill Version(s):

3.13.0 (source: frontmatter, pyproject.toml, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
