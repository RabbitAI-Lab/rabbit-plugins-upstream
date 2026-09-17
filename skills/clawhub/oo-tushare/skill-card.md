## Description:

Tushare helps agents search and read Tushare market data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Tushare market data, including stock listings, daily quotes, valuation indicators, adjustment factors, shareholder trades, and trading calendars through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback first-time setup path tells users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path before use and prefer a verified, signed, or checksum-validated oo CLI release.

Risk: Connector actions depend on account authentication, Tushare connection status, scopes, and billing state.

Mitigation: Run setup only after an auth or connection failure, and resolve expired credentials, missing scopes, or billing stops before retrying.

Risk: Actions that change or delete state would require extra care if such actions are added later.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Tushare Skill](https://clawhub.ai/oomol/skills/oo-tushare)
- [Tushare Homepage](https://tushare.pro)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas to validate request payloads and returns normalized tabular Tushare data when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
