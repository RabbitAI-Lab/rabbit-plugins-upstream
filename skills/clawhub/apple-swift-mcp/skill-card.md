## Description:

This skill helps agents use the native Swift MCP to work with Apple Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos data on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect and manage Apple app data on macOS, including calendar events, reminders, contacts, mail, messages, notes, maps, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private Calendar, Contacts, Mail, Messages, Notes, Photos, and Messages history data.

Mitigation: Install it only for trusted use cases, review macOS permission prompts carefully, and grant only permissions needed for the task.

Risk: The skill can create, update, send, import, export, or delete data in Apple apps.

Mitigation: Confirm sensitive actions before execution and review proposed writes, sends, exports, or deletions before allowing them.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include user-facing summaries of macOS app data and proposed create, update, send, import, export, or delete actions.]

## Skill Version(s):

1.4.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
