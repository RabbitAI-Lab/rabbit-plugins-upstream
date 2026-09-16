## Description:

CurrencyBeacon helps agents retrieve currency conversion, supported currency, latest exchange rate, historical rate, and timeseries rate data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query CurrencyBeacon data through the OOMOL oo CLI, including currency conversion, supported currencies, latest rates, historical rates, and rates across date ranges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Use a pinned, signed, or package-manager installation path for the oo CLI, or independently review and verify the installer source before execution.

Risk: CurrencyBeacon connector actions depend on live schemas and account connection state.

Mitigation: Inspect the action schema before building payloads and only run setup or connection steps after an auth or connection failure.

## Reference(s):

- [CurrencyBeacon homepage](https://currencybeacon.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-currencyscoop)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
