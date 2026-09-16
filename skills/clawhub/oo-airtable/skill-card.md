## Description:

Airtable (airtable.com). Use this skill for ANY Airtable request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to read Airtable bases, schemas, collaborators, and records, and to create, update, or delete Airtable bases, tables, fields, and records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer snippets can execute changing network code on a user's machine.

Mitigation: Avoid running remote installer snippets unless the oo CLI installation source is independently trusted and verified.

Risk: The skill can access sensitive Airtable data through the connected Airtable/OOMOL account.

Mitigation: Use an account whose permissions match the task and review the skill before installing in environments with sensitive Airtable data.

Risk: Write and destructive actions can change or delete Airtable bases, tables, fields, or records.

Mitigation: Confirm all write or delete payloads carefully and get explicit approval before destructive operations.

## Reference(s):

- [Airtable homepage](https://airtable.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Airtable ClawHub release](https://clawhub.ai/oomol/skills/oo-airtable)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.5 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
