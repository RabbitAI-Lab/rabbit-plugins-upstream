## Description:

chezmoi supports dotfile management workflows for interactive apply review, template consolidation, macOS and Windows compatibility checks, environment validation, MCP server synchronization, and SourceGit helper setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage chezmoi dotfiles: review diffs before applying changes, consolidate templates, fix macOS and Windows compatibility issues, validate required files, and synchronize MCP server configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SourceGit helper can launch Claude on repository contents while bypassing normal permission prompts.

Mitigation: Review or remove the helper before installation, and avoid permission-bypass and resume behavior for untrusted repositories.

Risk: Plaintext dotfile management can expose tokens or other secrets if they are stored in chezmoi-managed files.

Mitigation: Keep secrets out of plaintext chezmoi-managed files and review diffs before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/chezmoi)
- [Apply](artifact/apply.md)
- [Template Consolidation](artifact/consolidate.md)
- [Cross-Platform](artifact/cross-platform.md)
- [Diff Required](artifact/diff-required.md)
- [Doctor](artifact/doctor.md)
- [MCP Server Synchronization](artifact/mcp-sync.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-file approval prompts before applying chezmoi changes.]

## Skill Version(s):

0.4.3 (source: server release metadata and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
