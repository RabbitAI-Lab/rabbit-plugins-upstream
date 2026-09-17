## Description:

Grist (getgrist.com). Use this skill for ANY Grist request -- reading, creating, updating, and deleting data. Whenever a task involves Grist, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Grist through an OOMOL-connected account, including reading workspaces, documents, tables, columns, and records, and adding, updating, or deleting records after appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a live internet installer directly in a shell without verification.

Mitigation: Install only when the publisher is trusted, and review or replace the installer step with a verified installation path before deployment.

Risk: Write and destructive actions can change or remove Grist records.

Mitigation: Confirm the exact payload, target records, and expected effect with the user before running add, update, or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-grist)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Grist Homepage](https://www.getgrist.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON data with execution metadata; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
