## Description:

ERPNext (erpnext.com). Use this skill for ERPNext requests that read, create, update, or delete data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate ERPNext through an OOMOL-connected account, including document lookup, listing, counting, creation, updates, field changes, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional oo CLI installer uses a remote shell command.

Mitigation: Review the installer before running it and use the documented install guide when setup is required.

Risk: ERPNext write actions can create or modify business records.

Mitigation: Confirm the exact payload and expected effect with the user before running create, update, or set-value actions.

Risk: The delete action can remove ERPNext documents.

Mitigation: Require explicit user approval for the target DocType and document name before running destructive actions.

## Reference(s):

- [ClawHub ERPNext Skill](https://clawhub.ai/oomol/skills/oo-erpnext)
- [ERPNext Homepage](https://erpnext.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses may return JSON data with execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
