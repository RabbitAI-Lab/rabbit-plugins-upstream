## Description:

Oh My Zsh management for adding plugins to the .zshrc plugins array and authoring custom $ZSH_CUSTOM/*.zsh configuration files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Oh My Zsh plugins and custom shell configuration while preserving dotfile-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose changes to shell startup files such as .zshrc or files under $ZSH_CUSTOM.

Mitigation: Show diffs and get explicit user approval before modifying startup files or custom shell configuration.

Risk: The skill contains an automatic self-improvement instruction to run /skill-manager upgrade omz after use.

Mitigation: Do not run skill upgrades as part of ordinary Oh My Zsh configuration work unless the user gives separate consent.

## Reference(s):

- [Oh My Zsh Plugin Management](artifact/plugin.md)
- [Oh My Zsh Custom Script Authoring](artifact/custom.md)
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/omz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to shell startup files and Oh My Zsh custom files.]

## Skill Version(s):

0.3.4 (source: server release metadata and target metadata, released 2026-09-18 in changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
