## Description:

Oh My Zsh management for adding or installing plugins in .zshrc and authoring $ZSH_CUSTOM/*.zsh custom configuration files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and shell users use this skill to update Oh My Zsh plugins, install external plugins, and write custom aliases, functions, environment variables, or keybindings in $ZSH_CUSTOM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a self-improvement instruction that can ask the agent to run /skill-manager upgrade omz after normal use.

Mitigation: Do not allow the skill to run /skill-manager upgrade omz unless the user explicitly asked to update the skill.

Risk: The skill can propose changes to .zshrc or $ZSH_CUSTOM and may install external Oh My Zsh plugins.

Mitigation: Review the exact diff and any external plugin source before applying shell configuration changes or cloning plugin repositories.

## Reference(s):

- [Oh My Zsh Plugin Management](plugin.md)
- [Oh My Zsh Custom Script Authoring](custom.md)
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/omz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and zsh configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to .zshrc or $ZSH_CUSTOM/*.zsh and commands for installing or verifying Oh My Zsh plugins.]

## Skill Version(s):

0.3.3 (source: server release metadata and CHANGELOG, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
