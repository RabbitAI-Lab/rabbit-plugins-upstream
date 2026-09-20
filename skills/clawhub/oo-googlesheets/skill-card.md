## Description:

Google Sheets skill for reading, creating, updating, and deleting spreadsheet data through the OOMOL oo CLI and Google Sheets connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Google Sheets through an OOMOL-connected account, including spreadsheet discovery, range reads, row lookups, value writes, formatting, filters, validation, and sheet management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may ask the agent to run a remote oo CLI installer script.

Mitigation: Install only when the CLI is missing, and inspect or verify the OOMOL installer before running it.

Risk: Write and destructive Google Sheets actions can overwrite, clear, delete, or replace spreadsheet data.

Mitigation: Confirm the target spreadsheet, sheet, range, payload, and expected effect with the user before executing write or destructive actions.

Risk: The connector relies on OOMOL-managed account access for Google Sheets operations.

Mitigation: Use only with trusted OOMOL access and a connected Google Sheets account that is authorized for the data being accessed.

## Reference(s):

- [ClawHub Google Sheets Skill](https://clawhub.ai/oomol/skills/oo-googlesheets)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Google Sheets](https://workspace.google.com/products/sheets/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return normalized Google Sheets data, metadata, counters, batch replies, or range-focused response shapes.]

## Skill Version(s):

1.0.4 (source: evidence release version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
