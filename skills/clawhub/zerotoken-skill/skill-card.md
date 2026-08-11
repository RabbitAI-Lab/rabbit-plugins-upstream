## Description:

Token-efficient assistant discipline for concise answers and task execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phoenixlucky](https://clawhub.ai/user/phoenixlucky)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and agent users use ZeroToken to guide assistants toward concise task classification, targeted context gathering, and short actionable outputs. The skill also documents optional file-editing and encoding utility workflows for local development tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to read or modify local files, run local Python utilities, or perform Git operations.

Mitigation: Install only when these local development capabilities fit the workspace policy, and review proposed file or Git changes before applying them.

Risk: Bulk encoding repair utilities can modify many files and may alter text unexpectedly if run over an overly broad target.

Mitigation: Use preview and backup options where available, and limit encoding operations to the intended directory and file extensions.

Risk: Chinese-language and Windows/PowerShell guidance is environment-specific and could be inappropriate for other workflows.

Mitigation: Use the Chinese and Windows-specific mode only when the user explicitly opts in or the environment clearly requires it.

## Reference(s):

- [Unicode Encoding Specification](docs/unicode-encoding-spec.md)
- [ZeroToken ClawHub Skill Page](https://clawhub.ai/phoenixlucky/zerotoken-skill)
- [Publisher Profile](https://clawhub.ai/user/phoenixlucky)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be concise and task-focused.]

## Skill Version(s):

1.10.0 (source: server evidence, SKILL.md frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
