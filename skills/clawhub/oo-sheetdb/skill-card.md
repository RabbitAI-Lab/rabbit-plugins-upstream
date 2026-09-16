## Description:

SheetDB lets an agent inspect schemas and read, create, update, search, and delete rows in a connected SheetDB spreadsheet through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SheetDB-backed spreadsheets from an agent, including reading metadata and rows, searching records, and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI through a verified, version-pinned, or vendor-documented method before using the skill.

Risk: Write and destructive actions can change or remove SheetDB rows.

Mitigation: Confirm the exact action, payload, target column, matching value, and expected effect with the user before running write or delete commands.

Risk: Action inputs and outputs depend on the live SheetDB connector schema.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing payloads.

## Reference(s):

- [ClawHub SheetDB Skill Page](https://clawhub.ai/oomol/skills/oo-sheetdb)
- [SheetDB Homepage](https://sheetdb.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
