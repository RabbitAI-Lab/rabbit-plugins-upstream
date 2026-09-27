## Description:

Helps agents use Revdoku cloud storage and incoming email to store, share, and manage files and messages with authorized collaborators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emirn](https://clawhub.ai/user/emirn)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with authorized Revdoku access use this skill to store and share files, manage bucket versions, and read incoming email and attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Permanent bucket deletion is available without a separate local confirmation gate.

Mitigation: Require explicit approval before deletion and restrict credentials from permanently deleting buckets unless necessary.

Risk: Local file uploads and stored Revdoku credentials can expose data if used without authorization.

Mitigation: Confirm selected files and account access before uploading; protect locally stored credentials.

Risk: Archiving, restoring, or creating accounts can change shared data or access.

Mitigation: Require approval before archive, restore, or account creation.

## Reference(s):

- [Revdoku homepage](https://revdoku.com)
- [Revdoku API documentation](https://revdoku.com/api.md)
- [ClawHub skill listing](https://clawhub.ai/emirn/skills/revdoku)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and references to files and messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local CLI supports file uploads; hosted agent tools handle bucket text and incoming email.]

## Skill Version(s):

1.0.500 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
