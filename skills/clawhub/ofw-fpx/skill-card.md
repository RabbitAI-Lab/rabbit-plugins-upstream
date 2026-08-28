## Description:

ofw-fpx guides agents through using fpx to capture an OurFamilyWizard browser Bearer token and then issue curl requests for OFW messages, calendar, expenses, journal, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, external users, and agents use this skill to script OurFamilyWizard reads and carefully controlled writes from a shell when the ofw-mcp server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables shell-level access to sensitive OurFamilyWizard records using a captured browser session token.

Mitigation: Treat the token like a password, keep it out of logs and shared shell history, and recapture it only from an intentionally signed-in browser session.

Risk: The documented commands can perform real sends, deletes, uploads, expenses, calendar changes, and journal entries on a shared court-visible record.

Mitigation: Review every curl command before execution and require explicit confirmation before delegating write, delete, upload, expense, calendar, or journal actions.

Risk: Some reads can change account state, including marking unread inbox messages as read or updating dashboard last-seen status.

Mitigation: Warn users before state-changing reads and prefer list endpoints when only a preview is needed.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes direct API request examples and safety guidance for handling live OFW tokens and writes.]

## Skill Version(s):

2.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
