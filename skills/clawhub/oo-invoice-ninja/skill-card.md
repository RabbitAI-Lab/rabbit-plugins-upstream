## Description:

Invoice Ninja (invoiceninja.com). Use this skill for ANY Invoice Ninja request — reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to read, create, and update Invoice Ninja clients, invoices, and payments through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Invoice Ninja clients, invoices, and payments.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write actions.

Risk: Client contact updates may replace complete contact lists.

Mitigation: Inspect the live action schema and review the full contact payload before approving an update.

Risk: First-time setup may require installing the oo CLI.

Mitigation: Run the installer only from OOMOL sources that the user trusts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-invoice-ninja)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Invoice Ninja Homepage](https://invoiceninja.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
