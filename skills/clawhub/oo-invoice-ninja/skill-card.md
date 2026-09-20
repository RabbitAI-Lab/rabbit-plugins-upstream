## Description:

This skill lets an agent read, create, update, and delete Invoice Ninja records through an OOMOL-connected account instead of calling the Invoice Ninja API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to let an agent manage Invoice Ninja clients, invoices, and payments through OOMOL-connected account credentials. It supports listing and retrieving records, creating new clients, invoices, and payments, and updating clients or invoices when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Invoice Ninja account data, including creating payments and updating clients or invoices.

Mitigation: Inspect the live action schema, confirm the exact target and JSON payload with the user, and require explicit approval before write or destructive actions.

Risk: The first-time setup fallback includes shell installer commands for the oo CLI.

Mitigation: Install the oo CLI only from verified official instructions and avoid blindly running piped installer commands.

Risk: Using the skill delegates Invoice Ninja account operations to OOMOL-connected credentials.

Mitigation: Install and use the skill only when the user intends OOMOL to operate the connected Invoice Ninja account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-invoice-ninja)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Invoice Ninja homepage](https://invoiceninja.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
