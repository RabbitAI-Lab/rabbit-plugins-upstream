## Description:

Inspect Mermail API and email usage and manage workspaces, members, invitations, email domains, mailboxes, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to inspect Mermail workspace usage and safely manage members, invitations, domains, mailboxes, settings, and storage through the authenticated Mermail workspace boundary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real workspace administration changes when authorized with a Mermail API key.

Mitigation: Review the exact target resource, current state, and intended change before approving role, invitation, domain, mailbox, or settings writes.

Risk: Member removal and email domain deletion are destructive administrative actions.

Mitigation: Require explicit approval for the exact target and use the single-use destructive-action token described by the skill before execution.

Risk: Mailbox creation can consume provision credits and may duplicate an existing mailbox if discovery is skipped.

Mitigation: List existing mailboxes first, reuse an exact suitable match, and make only one explicitly authorized provision.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Workspace administration tool map](references/tools.md)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-administer-workspace)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown reports, proposals, diffs, and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses exact returned resource identifiers, values, limits, statuses, and approval state when reporting administrative outcomes.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
