## Description:

Operate ChartMogul through OOMOL's oo CLI to search and read account, customer, contact, and source data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to retrieve ChartMogul account, customer, contact, and data-source information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer pipe commands for the oo CLI.

Mitigation: Review the setup path before installing and prefer a pinned, verified release or trusted package manager.

Risk: The skill can retrieve ChartMogul account and customer data through an OOMOL-connected account.

Mitigation: Confirm the ChartMogul connection is approved for the intended workspace and limit access to users who are allowed to view that data.

## Reference(s):

- [ChartMogul homepage](https://chartmogul.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chartmogul)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; read actions return data with execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
