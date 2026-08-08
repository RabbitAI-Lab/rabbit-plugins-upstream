## Description:

Inspect Mermail API and email usage and manage workspaces, members, invitations, email domains, mailboxes, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and operators use this skill to inspect Mermail workspace state and safely perform membership, invitation, email-domain, mailbox, storage, plan-usage, RPM, and credit-management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses MERMAIL_API_KEY to administer a Mermail workspace.

Mitigation: Install it only when workspace administration is intended, and keep the API key scoped and protected according to Mermail account policy.

Risk: Destructive actions such as workspace deletion, member removal, and domain deletion can materially change access or routing.

Mitigation: Preview the impact, require explicit approval, call prepare_destructive_action with exact arguments, and execute only once with the returned token.

Risk: Mailbox provisioning can create duplicates or consume provision credits.

Mitigation: List existing mailboxes first, reuse exact matches, verify required fields, and check usage or credits before large or costly workflows.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [ClawHub Skill Release Page](https://clawhub.ai/mermail/skills/mermail-administer-workspace)
- [Workspace Administration Tool Map](artifact/references/tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and tool-call driven responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses MERMAIL_API_KEY and the Mermail MCP server for workspace administration workflows.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
