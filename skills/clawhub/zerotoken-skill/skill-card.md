## Description:

Token-efficient assistant discipline for concise, direct answers and minimal-context task execution, with optional local file-encoding and Windows PowerShell utilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phoenixlucky](https://clawhub.ai/user/phoenixlucky)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and agent users use ZeroToken to guide assistants toward concise, task-focused responses, bounded context gathering, and predictable workflows. The bundled utilities support local encoding checks, encoding repair workflows, version checks, and Windows PowerShell-safe file handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Encoding repair and conversion utilities can recursively overwrite files, and backups are not enforced.

Mitigation: Run utilities on scoped paths, review scan or preview output first, and keep version control or separate backups before write operations.

Risk: Environment detection can persist workspace details in .zerotoken/environment.json.

Mitigation: Confirm local policy allows this workspace metadata before enabling persistence, and remove the file when it is not needed.

## Reference(s):

- [ZeroToken README](README.md)
- [Skill Definition](SKILL.md)
- [Tool Mapping](references/tool-mapping.md)
- [Windows PowerShell Guidance](references/windows-powershell.md)
- [Unicode Encoding Specification](docs/unicode-encoding-spec.md)
- [ClawHub Skill Page](https://clawhub.ai/phoenixlucky/skills/zerotoken-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise, user-facing responses with optional local utility commands.]

## Skill Version(s):

1.14.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
