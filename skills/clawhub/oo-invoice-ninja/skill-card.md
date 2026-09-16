## Description:

Use this skill to read, create, and update Invoice Ninja clients, invoices, and payments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Invoice Ninja customer, invoice, and payment workflows through live connector schemas and oo CLI actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that can execute local code.

Mitigation: Install the oo CLI from a trusted, versioned source and verify it where possible before connecting Invoice Ninja or billing data.

Risk: Write actions can create or update Invoice Ninja clients, invoices, and payments.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged [write].

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-invoice-ninja)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Invoice Ninja homepage](https://invoiceninja.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses containing data and execution metadata when run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
