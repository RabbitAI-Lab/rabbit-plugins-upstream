## Description:

Securely connects agents such as WorkBuddy, OpenClaw, Codex, and Claude to Super Diary so they can query records, trends, summaries, and trip notes, creating new entries only after explicit user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents connect to a configured Super Diary account, search and summarize diary records across sources and time ranges, and add notes only after confirming the content, timestamp, and sharing state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read private diary content through the configured key.

Mitigation: Install only when the diary service and package source are trusted, keep the key out of public logs and repositories, and narrow searches by date or keyword before reading records.

Risk: An agent could create a diary note with unintended content or sharing state.

Mitigation: Create notes only after restating the content, timestamp, and sharing state and receiving explicit confirmation for the current write.

Risk: The required connector is installed from a GitHub package archive.

Mitigation: Review the package source before installation and use the skill's doctor check to confirm the configured connection after install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/super21-bat/skills/diary-agent-control)
- [Project homepage](https://github.com/super21-bat/diary-agent-control)
- [Node install package archive](https://github.com/super21-bat/diary-agent-control/archive/refs/heads/main.tar.gz)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP connection guidance, diary query commands, and explicit confirmation steps before note creation.]

## Skill Version(s):

0.6.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
