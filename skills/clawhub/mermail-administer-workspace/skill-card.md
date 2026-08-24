## Description:

Inspect Mermail API and email usage and manage workspaces, members, invitations, email domains, mailboxes, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to inspect Mermail workspace usage and safely administer members, invitations, domains, mailboxes, settings, storage, credits, and usage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer a Mermail workspace using the permissions granted to MERMAIL_API_KEY.

Mitigation: Install it only for intended Mermail workspace administration and keep actions within the credential-bound workspace.

Risk: Member removals, domain deletion, role changes, invitations, and mailbox provisioning can affect access, routing, or credits.

Mitigation: Review exact current-to-intended previews before writes; require explicit approval for destructive actions and verify affected resources after changes when read endpoints are available.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Administer Mermail Workspace on ClawHub](https://clawhub.ai/mermail/skills/mermail-administer-workspace)
- [Workspace Administration Tool Map](references/tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown and concise text reports with current-state evidence, proposed changes, approvals, and verification status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stable workspace, member, domain, mailbox, and usage identifiers when needed to distinguish targets.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
