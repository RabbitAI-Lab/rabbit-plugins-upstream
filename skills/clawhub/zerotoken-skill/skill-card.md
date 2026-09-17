## Description:

ZeroToken guides agents toward concise, direct answers and minimal-context task execution, with optional local utilities for file encoding, Windows PowerShell handling, audits, version checks, and batch edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phoenixlucky](https://clawhub.ai/user/phoenixlucky)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and agent users use ZeroToken to reduce unnecessary context loading, tool calls, and verbose responses while preserving task accuracy. It also provides local scripts for encoding safety, environment detection, documentation audits, and release consistency checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment detection can persist host environment details in a local .zerotoken/environment.json cache.

Mitigation: Review the cached file before sharing workspaces or artifacts, and remove it when environment details should not persist.

Risk: Encoding and batch-edit utilities can recursively modify local files.

Mitigation: Run these utilities only in version-controlled or backed-up directories, inspect target paths first, and review diffs before committing changes.

## Reference(s):

- [ZeroToken ClawHub Skill Page](https://clawhub.ai/phoenixlucky/skills/zerotoken-skill)
- [Unicode Encoding Specification](docs/unicode-encoding-spec.md)
- [Windows PowerShell Guidance](references/windows-powershell.md)
- [Refactor Playbook](references/refactor-playbook.md)
- [Search Guidance](references/search.md)
- [Tool Mapping](references/tool-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional code blocks, shell commands, JSON reports, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Favors concise, task-focused output; bundled utilities may emit JSON when called with --json.]

## Skill Version(s):

1.14.0 (source: frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
