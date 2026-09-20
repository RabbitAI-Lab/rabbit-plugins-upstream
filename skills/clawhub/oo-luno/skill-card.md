## Description:

Luno (luno.com). Use this skill for Luno requests that search or read account, order, ticker, order book, and trade data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve read-only Luno account and market information through the oo CLI, including balances, orders, tickers, order book levels, and recent trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback first-time setup path asks users to install the oo CLI with a remotely fetched shell or PowerShell script.

Mitigation: Review the oo CLI installation path before installing and prefer verified manual installation from trusted OOMOL documentation.

Risk: Connecting Luno grants OOMOL connector access to read account balances and order information.

Mitigation: Connect Luno only after confirming that this account-level read access is acceptable for the intended use.

## Reference(s):

- [ClawHub Luno Skill](https://clawhub.ai/oomol/skills/oo-luno)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Luno Homepage](https://www.luno.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
