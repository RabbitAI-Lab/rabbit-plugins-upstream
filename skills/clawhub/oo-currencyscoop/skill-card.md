## Description:

CurrencyBeacon helps agents convert currencies and retrieve supported, latest, historical, and timeseries exchange-rate data through the OOMOL currencyscoop connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up CurrencyBeacon currency data, including conversions, supported currencies, current rates, historical rates, and timeseries rates, without handling raw CurrencyBeacon API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer scripts are presented for first-time oo CLI setup and may be run directly in a shell.

Mitigation: Install the oo CLI through a verified official package when possible, or download and inspect the installer before running it.

Risk: CurrencyBeacon access depends on an intentional OOMOL account connection and valid credentials.

Mitigation: Connect CurrencyBeacon through OOMOL only when needed and retry setup steps only after authentication, scope, expiration, or app connection errors.

## Reference(s):

- [CurrencyBeacon homepage](https://currencybeacon.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-currencyscoop)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running CurrencyBeacon actions; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
