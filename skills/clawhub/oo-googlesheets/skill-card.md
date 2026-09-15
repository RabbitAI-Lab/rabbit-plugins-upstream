## Description:

Enables agents to operate Google Sheets through the OOMOL oo CLI for reading, creating, updating, searching, formatting, and managing spreadsheet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Google Sheets action schemas and run read, write, formatting, search, filtering, chart, validation, metadata, and sheet-management operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run remote installer scripts directly in a shell.

Mitigation: Review the OOMOL CLI installation path and prefer official, versioned instructions with checksum or signature verification before running an installer.

Risk: Write and destructive Google Sheets actions can alter, overwrite, or remove spreadsheet data.

Mitigation: Confirm exact payloads and intended effects before write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Google Sheets Skill](https://clawhub.ai/oomol/skills/oo-googlesheets)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Google Sheets](https://workspace.google.com/products/sheets/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON payloads, and structured command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing connector payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
