## Description:

Helps agents retrieve accounting records and create or update user-approved entries in Money Forward Cloud Accounting through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Accounting staff and developers with an OOMOL-connected Money Forward account can inspect offices, accounts, journals, transactions, and reports, and create or update accounting entries with user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested remote installer scripts could run unreviewed code on the user's machine.

Mitigation: Install the oo CLI through a trusted package manager or verified official instructions instead of running remote scripts through an agent.

Risk: Creating or replacing accounting records can cause incorrect or duplicate ledger entries.

Mitigation: Require explicit approval of the office, payload, and expected ledger effect before each write; check the ledger before retrying an uncertain write.

## Reference(s):

- [Money Forward Cloud Accounting MCP documentation](https://developers.biz.moneyforward.com/mcp/)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [oo CLI repository (tooling)](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill release](https://clawhub.ai/oomol/skills/oo-moneyforward-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Text responses and structured accounting results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on office access and available accounting data.]

## Skill Version(s):

1.0.0 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
