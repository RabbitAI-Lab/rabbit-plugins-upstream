## Description:

ERPNext helps agents read, create, update, and delete ERPNext data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ERPNext records through authenticated OOMOL connections, including document reads, counts, field lookups, creates, updates, and deletes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded scripts without verification.

Mitigation: Install the oo CLI from a verified, versioned source or inspect and verify the installer before execution.

Risk: Write and delete actions can change or remove ERPNext records.

Mitigation: Confirm the exact records, action, and payload before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ERPNext homepage](https://erpnext.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-erpnext)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with oo CLI shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing ERPNext actions require user confirmation; destructive actions require explicit approval.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
