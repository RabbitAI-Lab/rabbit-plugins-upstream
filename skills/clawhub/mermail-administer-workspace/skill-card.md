## Description:

Inspect Mermail AI, API, and email usage and manage workspaces, members, invitations, email domains, mailboxes, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and authorized support operators use this skill to inspect Mermail usage, storage, members, domains, mailboxes, and settings, then make approved administrative changes within the authenticated workspace boundary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform administrative changes using privileges tied to MERMAIL_API_KEY.

Mitigation: Install only for intended Mermail workspace administration and review proposed member, domain, mailbox, and settings changes before approval.

Risk: Sensitive actions such as removals, domain deletion, role changes, and automatic-response settings can have workspace-wide effects.

Mitigation: Require exact target previews, explicit approval, and the skill's destructive-action token flow where applicable.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP Server](https://console.mermail.app/mcp)
- [Workspace administration tool map](references/tools.md)
- [Workspace AI credits](references/ai-credits.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports exact workspace state, current-to-intended diffs, approval status, and verification outcomes.]

## Skill Version(s):

1.2.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
