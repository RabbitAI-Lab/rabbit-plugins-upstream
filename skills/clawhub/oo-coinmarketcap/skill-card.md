## Description:

CoinMarketCap lets agents search and read cryptocurrency market data through the CoinMarketCap connector using the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve CoinMarketCap market data, cryptocurrency identifiers, quotes, listings, global metrics, key usage information, and price conversions through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup tells users to run a remote OOMOL installer script directly in a shell.

Mitigation: Review the oo CLI installation path before use, prefer a pinned package or verified installer from OOMOL, inspect downloaded scripts before execution, and avoid administrator privileges unless OOMOL clearly requires them.

Risk: The skill depends on an authenticated OOMOL account connected to CoinMarketCap.

Mitigation: Use the normal read connector actions after sign-in, avoid handling raw credentials, and reconnect only when the oo CLI reports an authentication or connection error.

## Reference(s):

- [CoinMarketCap ClawHub skill page](https://clawhub.ai/oomol/skills/oo-coinmarketcap)
- [CoinMarketCap homepage](https://coinmarketcap.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the OOMOL oo CLI, a signed-in OOMOL account, and a connected CoinMarketCap account.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
