## Description:

Freshstatus (freshworks.com). Use this skill for ANY Freshstatus request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Freshstatus status-page services and service groups through an OOMOL-connected account. It supports reading, creating, updating, and deleting Freshstatus resources while prompting for confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Freshstatus services and service groups through the OOMOL CLI.

Mitigation: Use an OOMOL/Freshstatus account with permissions limited to the intended work and require explicit user confirmation for every write or delete action.

Risk: The setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Review installation steps before use and prefer a verified or package-manager installation path instead of piping remote scripts directly into a shell.

## Reference(s):

- [Freshstatus homepage](https://www.freshworks.com/statuspage)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect live Freshstatus action schemas and execute Freshstatus connector actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
