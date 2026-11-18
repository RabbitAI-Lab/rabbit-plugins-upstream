## Description:

Sets up, migrates, themes, checks, syncs, updates, and uninstalls a macOS terminal workbench and its shell configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers using macOS can use the skill to configure or migrate their terminal environment, manage themes, diagnose setup issues, and export or restore settings. It produces shell commands and configuration changes for the user's explicitly requested terminal tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious: routine diagnostics may run the user's shell startup code, and some cleanup, uninstall, or rollback paths may alter unrelated configuration; scan coverage is partial.

Mitigation: Review the relevant scripts and planned changes before running them, use dry-run modes where available, and keep configuration backups.

## Reference(s):

- [Product home](https://huiyonghkw.github.io/hekouwang-terminal-lite-skill/index.html?lang=en)
- [Product guide](https://huiyonghkw.github.io/hekouwang-terminal-lite-skill/guide/index.html?lang=en)
- [First-run guide](artifact/references/first-run.md)
- [iTerm2 GUI settings](artifact/references/iterm2-gui-settings.md)
- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-terminal-lite-skill)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Shell commands, configuration files, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and changes depend on the user's requested terminal task and supplied paths.]

## Skill Version(s):

3.0.5 (source: server-resolved release metadata and artifact/SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
