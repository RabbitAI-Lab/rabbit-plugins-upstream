## Description:

Helps agents read and manage QuickBooks Online accounting records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Accountants, business users, and their agents can retrieve QuickBooks Online reports and records, and create or update accounting transactions after reviewing the intended changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accounting writes, deletions, voids, and batches can change or irreversibly remove financial records.

Mitigation: Review the exact payload and effect before writes; confirm the target and obtain explicit approval for destructive actions.

Risk: One-line remote installer commands execute downloaded code.

Mitigation: Independently verify the oo CLI installer source and integrity before running installation commands.

## Reference(s):

- [QuickBooks Online skill release](https://clawhub.ai/oomol/skills/oo-quickbooks)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [QuickBooks Online](https://quickbooks.intuit.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and summaries of QuickBooks results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account access requires an OOMOL-connected QuickBooks Online account.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
