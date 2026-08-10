## Description:

chezmoi dotfile management guidance for interactive diff review, template consolidation, cross-platform compatibility, environment checks, MCP synchronization, and SourceGit-related workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage chezmoi dotfiles, review diffs before applying changes, consolidate shared templates, diagnose macOS and Windows compatibility issues, and synchronize MCP server configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled SourceGit launcher starts Claude Code with permission checks disabled.

Mitigation: Do not install or invoke bin/claude-source.sh unless that bypass behavior is explicitly accepted; prefer a launcher that keeps permission checks enabled.

Risk: Plaintext tokens in chezmoi-managed files could be propagated into dotfile outputs.

Mitigation: Use encrypted secret handling or separate environment files that are not managed as plaintext chezmoi templates.

Risk: Applying generated dotfile changes without reviewing the rendered diff could overwrite local configuration.

Mitigation: Run chezmoi diff, show the relevant diff to the user, and apply only files the user approves.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/chezmoi)
- [SKILL.md](SKILL.md)
- [Apply guide](apply.md)
- [Template consolidation guide](consolidate.md)
- [Cross-platform guide](cross-platform.md)
- [Doctor guide](doctor.md)
- [MCP sync guide](mcp-sync.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes showing chezmoi diffs and obtaining user approval before applying changes.]

## Skill Version(s):

0.4.1 (source: server release metadata and CHANGELOG.md, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
