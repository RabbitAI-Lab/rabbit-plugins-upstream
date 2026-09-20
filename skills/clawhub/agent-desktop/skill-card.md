## Description:

Reliable computer use via native OS accessibility trees for agents that need to observe and operate desktop applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to let an AI agent inspect desktop UI state, run scoped desktop automation commands, and verify GUI interactions across observation, interaction, app lifecycle, clipboard, notification, wait, and session workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad local desktop automation through a CLI.

Mitigation: Install and use it only for explicit desktop automation tasks where the operator is comfortable granting that level of local control.

Risk: Screenshots, clipboard contents, traces, and exported replay artifacts can contain sensitive local data.

Mitigation: Treat those outputs as sensitive, prefer `--no-trace` or cleanup commands for sensitive work, and opt in to screenshot artifacts only when needed.

Risk: Forced or physical input can deliver shortcuts or pointer actions with side effects.

Mitigation: Prefer scoped app and ref-based commands, avoid `--force` unless the shortcut is intentionally being delivered, and verify UI state after actions.

Risk: Desktop automation depends on platform permissions and currently documented macOS adapter behavior.

Mitigation: Check permissions before use, grant Accessibility and Screen Recording only when required, and account for Windows and Linux support being planned rather than documented as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Observation commands](references/commands-observation.md)
- [Interaction commands](references/commands-interaction.md)
- [System commands](references/commands-system.md)
- [Common automation workflows](references/workflows.md)
- [macOS platform notes](references/macos.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent in invoking a local CLI that returns structured JSON envelopes and may create local screenshots, traces, and session artifacts when requested.]

## Skill Version(s):

0.1.31 (source: server release metadata; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
