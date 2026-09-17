## Description:

CoinGecko lets an agent search and retrieve CoinGecko market, coin, token, pool, ticker, price, chart, OHLC, and global cryptocurrency data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they need CoinGecko cryptocurrency market data, token metadata, onchain pool information, and discovery queries from a connected CoinGecko account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that should be reviewed before use.

Mitigation: Review the oo CLI installation path before installing, prefer official manual installation or verified releases, validate checksums or signatures when available, and avoid running the installer with administrator or root privileges.

Risk: CoinGecko requests and connector payloads pass through OOMOL using the connected account.

Mitigation: Use an appropriate OOMOL account connection and avoid sending queries or payloads that expose data the connected account should not process.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-coingecko)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [CoinGecko Homepage](https://www.coingecko.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CoinGecko data retrieval; available history, intervals, and page depth can depend on the connected CoinGecko plan.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
