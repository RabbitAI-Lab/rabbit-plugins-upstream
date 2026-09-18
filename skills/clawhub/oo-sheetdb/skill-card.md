## Description:

This skill manages SheetDB (sheetdb.io) requests, including reading, creating, updating, and deleting data through the OOMOL-connected SheetDB connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SheetDB spreadsheet structure, list and search rows, count records, and perform confirmed create, update, or delete operations through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions use remote installer scripts that run directly in a shell.

Mitigation: Review the setup path before installation; download the oo CLI installer from a trusted release channel and verify its checksum or signature before execution.

Risk: Create, update, and delete actions can change or remove SheetDB spreadsheet data.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [SheetDB homepage](https://sheetdb.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sheetdb)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected SheetDB account for live actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
