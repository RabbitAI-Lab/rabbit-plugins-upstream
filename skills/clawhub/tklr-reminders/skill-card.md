## Description:

tklr-reminders helps Hermes Agent manage calendars, schedules, events, appointments, tasks, reminders, and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[37rb](https://clawhub.ai/user/37rb)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill through Hermes Agent to manage personal schedules, tasks, notes, recurring reminders, and alert delivery in plain language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates persistent files, scheduled dispatcher behavior, and delivery commands on the user's machine.

Mitigation: Install it only when the user wants Hermes and tklr reminder management, and review the configured dispatcher and alert channels before relying on it.

Risk: Stored alert commands can execute later when reminders fire.

Mitigation: Avoid broad or raw command routes unless they are understood, and keep alert channel commands limited to intended delivery actions.

Risk: Misconfigured alert channels can make a reminder appear sent even when no message reaches the user.

Mitigation: Verify setup with the skill's status and test-alert flow, and review email or chat channel configuration before using reminders for important events.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/37rb/skills/tklr-reminders)
- [clawdis homepage](https://github.com/37Rb/hermes-skills/tree/main/skills/tklr-reminders)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [tklr](https://github.com/dagraham/tklr-dgraham)
- [tklr documentation](https://dagraham.github.io/tklr-dgraham/)
- [How it works](references/how-it-works.md)
- [Setup](references/setup.md)
- [Using the wrapper](references/using-the-wrapper.md)
- [tklr syntax](references/tklr-syntax.md)
- [Alerts configuration example](templates/alerts-config-example.toml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain-language text or Markdown for the user, plus local command execution and configuration updates by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Hermes Agent and tklr; supported on Linux and macOS.]

## Skill Version(s):

1.0.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
