## Description:

A Hermes Agent skill for managing calendars, schedules, events, appointments, tasks, and reminder alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[37rb](https://clawhub.ai/user/37rb)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through Hermes Agent to create, update, query, and complete reminders, calendar events, tasks, goals, notes, and time jots in plain language. The skill can configure local reminder delivery through chat, email, SMS, or desktop channels when supported by the user's environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup makes persistent local changes, including installing software, creating a tklr workspace, copying a dispatcher, and scheduling an every-minute reminder job.

Mitigation: Install only on trusted machines and review the setup status before relying on reminder delivery.

Risk: Misconfigured alert destinations or persisted alert commands can mark reminders as sent even when nobody receives the message.

Mitigation: Confirm the destination channel yourself and review alert commands before enabling or changing delivery routes.

Risk: Reset behavior can delete all reminders when used without care.

Mitigation: Use reset.sh --dry-run before any reset and confirm the affected workspace before destructive cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/37rb/skills/tklr-reminders)
- [Project homepage](https://github.com/37Rb/hermes-skills/tree/main/skills/tklr-reminders)
- [README](README.md)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [tklr project](https://github.com/dagraham/tklr-dgraham)
- [tklr documentation](https://dagraham.github.io/tklr-dgraham/)
- [How it works](references/how-it-works.md)
- [Setup guide](references/setup.md)
- [Wrapper usage](references/using-the-wrapper.md)
- [tklr syntax reference](references/tklr-syntax.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain-language text or Markdown, with shell commands and local configuration changes executed by the agent when setup or reminder operations require them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Hermes Agent on Linux or macOS with the hermes and tklr command-line tools available or installable.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
