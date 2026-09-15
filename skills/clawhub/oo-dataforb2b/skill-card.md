## Description:

DataForB2B helps agents search, count, and enrich people and company records through an OOMOL-connected DataForB2B account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect DataForB2B action schemas and run search, count, enrichment, account status, and typeahead actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Review the installer source and install the oo CLI through a verified, trusted channel before use; do not let an agent run the installer automatically unless the user explicitly accepts executing remote code from OOMOL.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dataforb2b)
- [DataForB2B Homepage](https://dataforb2b.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
