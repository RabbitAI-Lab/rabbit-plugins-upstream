## Description:

Guides agents in managing Basecamp projects, to-dos, messages, schedules, and documents through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and their agents use this skill to find and manage Basecamp projects, tasks, discussions, schedules, and documents, with user approval for changes and account connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-account access can expose or change Basecamp business data.

Mitigation: Prefer OAuth, limit access to the task, and confirm each write or deletion with the user.

Risk: Trigger destinations can forward event data to third-party hosts.

Mitigation: Use only destinations the user explicitly trusts and remove unused triggers and destinations.

Risk: Long-lived API keys or unattended automations can retain access beyond the task.

Mitigation: Prefer OAuth through the Maton CLI and remove unused connections and functions.

## Reference(s):

- [Basecamp 4 API documentation](https://github.com/basecamp/bc3-api)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Basecamp skill release](https://clawhub.ai/byungkyu/skills/basecamp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require a connected account and network access.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
