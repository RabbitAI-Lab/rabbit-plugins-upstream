## Description:

Oh My Zsh management for adding plugins to the .zshrc plugins array and writing $ZSH_CUSTOM/*.zsh configuration files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Oh My Zsh plugins, author shell aliases, functions, environment variables, and key bindings, and keep related dotfiles in sync when applicable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to modify shell startup configuration such as .zshrc or $ZSH_CUSTOM/*.zsh files.

Mitigation: Review the exact diff before applying changes and reload the shell only after the intended edits are confirmed.

Risk: External Oh My Zsh plugins are third-party shell code.

Mitigation: Inspect plugin repositories and pin or approve sources before cloning them into $ZSH_CUSTOM/plugins.

Risk: The self-improvement section can trigger a skill upgrade action after use.

Mitigation: Remove that section before deployment or require explicit human approval before running `/skill-manager upgrade omz`.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/omz)
- [Oh My Zsh Plugin Management](plugin.md)
- [Oh My Zsh Custom Script Authoring](custom.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and Zsh configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose .zshrc edits and $ZSH_CUSTOM/*.zsh file content for review before execution.]

## Skill Version(s):

0.3.2 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
