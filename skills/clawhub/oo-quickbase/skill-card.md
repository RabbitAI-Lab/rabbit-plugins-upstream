## Description:

Quickbase (quickbase.com). Use this skill for ANY Quickbase request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Quickbase apps and tables, query records, and run guarded create, update, or delete actions through an OOMOL-connected Quickbase account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute a remote installer immediately.

Mitigation: Review the installer path before use; prefer a signed or version-pinned install method, or download and inspect the installer before running it.

Risk: Write and delete actions can change or remove Quickbase records.

Mitigation: Only approve write or delete commands after checking the exact table, record IDs, and payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-quickbase)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Quickbase](https://www.quickbase.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands that inspect schemas, run Quickbase connector actions, and report execution IDs from command output.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
