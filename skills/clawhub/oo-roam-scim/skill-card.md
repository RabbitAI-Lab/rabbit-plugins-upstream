## Description:

Roam SCIM helps agents read, create, update, and delete Roam SCIM data through OOMOL's oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to manage Roam SCIM users and groups, including reads, creates, replacements, archival/reactivation, deletion/archive operations, and group membership updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented pipe-to-shell installer commands could execute arbitrary local code.

Mitigation: Use a signed or checksum-verified installer when available, and inspect downloaded installer scripts before execution.

Risk: Write and destructive SCIM actions can change, archive, or delete Roam users and groups.

Mitigation: Fetch the live connector schema, review the exact payload and target, and require explicit user approval before executing state-changing actions.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Roam homepage](https://ro.am)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before state-changing Roam SCIM actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
