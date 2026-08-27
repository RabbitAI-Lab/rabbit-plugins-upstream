## Description:

A structured command-line tool for managing your ideas, proposals, todos, and wishlist items with validation and drift prevention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kens-agents](https://clawhub.ai/user/kens-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to maintain a durable IDEAS.md list for ideas, proposals, todos, and wishlist items while keeping entries consistently formatted and searchable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and changes a persistent IDEAS.md file, and an ambiguous request or target path can update the wrong idea list.

Mitigation: Be explicit about the target file, use --file when managing a non-default list, and review the affected file after state-changing operations.

Risk: Delete operations permanently remove entries and the skill has no built-in undo.

Mitigation: Confirm the exact ID before deleting, record a decision reason, and rely on backups or version control for recovery.

Risk: Archive operations remove completed entries from IDEAS.md and reindex remaining IDs, which can change references.

Mitigation: Review archive behavior before confirming, avoid --force unless intentional, and check the printed ID mapping and archive file.

Risk: Broad idea-management trigger phrases can lead an agent to perform reporting or maintenance actions when the user expected only discussion.

Mitigation: Confirm user intent before write, edit, delete, or archive actions, especially when the request is conversational or underspecified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kens-agents/skills/idea-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [CLI text, Markdown reports, JSON exports, shell command invocations, and workspace file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads and writes IDEAS.md, can create memory/IDEAS-Archive-YYYY-MM-DD.md, and supports --file for alternate target files.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
