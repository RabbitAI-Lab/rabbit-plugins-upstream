## Description:

Financial Modeling Prep (financialmodelingprep.com) helps agents search and read market, company, financial statement, valuation, analyst, insider, SEC, and economic data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve Financial Modeling Prep data for securities research, market monitoring, financial statement review, valuation checks, economic indicator lookup, and related data queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts for the oo CLI.

Mitigation: Before installation, use a verified or package-manager installation route where available, run setup from an unprivileged shell, and review the remote installer path.

Risk: Financial Modeling Prep queries are routed through an OOMOL-connected account.

Mitigation: Confirm trust in the OOMOL account connection and understand the data-routing model before sending financial data queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-financial-modeling-prep)
- [Financial Modeling Prep Homepage](https://financialmodelingprep.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector commands return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
