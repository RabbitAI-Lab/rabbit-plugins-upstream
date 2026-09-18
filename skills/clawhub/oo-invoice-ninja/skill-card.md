## Description:

Invoice Ninja support for reading, creating, and updating client, invoice, and payment data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect live Invoice Ninja connector schemas and run client, invoice, and payment actions through an OOMOL-connected account. It supports read workflows and write workflows that require confirmation before changing Invoice Ninja data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute a remote installer directly.

Mitigation: Prefer an official signed package or download the installer separately, verify its source and checksum or signature when available, inspect it, and run it only with normal user privileges.

Risk: Write actions can change Invoice Ninja clients, invoices, or payments.

Mitigation: Confirm the exact target records, payload, and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Invoice Ninja skill page](https://clawhub.ai/oomol/skills/oo-invoice-ninja)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Invoice Ninja homepage](https://invoiceninja.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
