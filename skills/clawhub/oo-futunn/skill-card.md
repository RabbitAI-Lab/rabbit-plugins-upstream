## Description:

Helps agents read Futunn account, market, and research data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents with a connected Futunn account can review balances, positions, orders, market data, company financials, and related news without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a downloaded installer script directly in a shell.

Mitigation: Review the installation path and prefer a trusted package manager or verified installer guide before installing the oo CLI.

Risk: The connected skill can read sensitive account balances, positions, and orders.

Mitigation: Limit access to authorized users and avoid sharing account details beyond the requested task.

## Reference(s):

- [Futunn homepage](https://open.futunn.com)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [oo CLI tool reference](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of requested data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's connected Futunn access.]

## Skill Version(s):

1.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
