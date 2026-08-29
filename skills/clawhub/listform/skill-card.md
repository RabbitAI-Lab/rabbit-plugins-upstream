## Description:

List is a smart form and notes skill that records bookkeeping entries, shipments, operational logs, notes, and attachments, then supports classification, querying, summaries, and reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to capture everyday expenses, notes, shipments, logs, receipt images, and document references in structured records. It is intended for quick entry, later lookup, recurring summaries, and reminders around personal or business recordkeeping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may record sensitive personal, business, receipt, contract, or operational information.

Mitigation: Review before installation, make auto-save and attachment analysis behavior clear to users, and avoid storing sensitive data unless the deployment has appropriate consent and retention controls.

Risk: The helper script can escape its intended data folder and copy arbitrary local files into persistent storage.

Mitigation: Restrict record type names, confine file writes to the skill data directory, and limit attachments to explicit user-provided uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/listform)
- [ClawHub publisher profile](https://clawhub.ai/user/kobenfang)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown responses, with JSON record data handled by the bundled command-line helper.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local JSON records and attachment copies when installed and invoked by an agent.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
