## Description:

Oh My Zsh management for adding plugins to .zshrc and writing custom $ZSH_CUSTOM/*.zsh configuration files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and shell users use this skill to manage Oh My Zsh plugins and author persistent custom zsh aliases, functions, environment variables, and key bindings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to modify persistent shell startup configuration in .zshrc or $ZSH_CUSTOM files.

Mitigation: Inspect diffs before applying changes, keep a backup of shell configuration, and test changes in a new terminal session before relying on them.

Risk: The source includes conversation-driven self-upgrade behavior.

Mitigation: Remove or disable the self-upgrade instruction unless explicit ongoing skill maintenance is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/omz)
- [Oh My Zsh plugin management](plugin.md)
- [Oh My Zsh custom script authoring](custom.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline shell and zsh code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed edits or commands that modify .zshrc and files under $ZSH_CUSTOM.]

## Skill Version(s):

0.3.1 (source: server release metadata, target metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
