## Description:

Retable lets an agent read, create, update, search, and delete Retable data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Retable workspaces, projects, tables, and rows from an agent session after connecting Retable through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI can access the user's connected Retable account.

Mitigation: Install and use the skill only when that account access is acceptable for the task.

Risk: One-time installer commands may execute downloaded scripts.

Mitigation: Prefer verifying or manually installing the oo CLI from OOMOL's official installation instructions.

Risk: Write and delete actions can change or remove Retable data.

Mitigation: Review exact write and delete payloads and get explicit approval before execution.

## Reference(s):

- [Retable homepage](https://www.retable.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Retable skill page](https://clawhub.ai/oomol/skills/oo-retable)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON from the oo CLI when run with --json.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
