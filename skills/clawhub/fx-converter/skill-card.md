## Description:

Provides real-time exchange-rate lookup and currency conversion using Frankfurter API data based on ECB reference rates, covering USD, CNY, EUR, JPY, and other major currencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and command-line users use this skill to query current foreign-exchange rates, convert amounts between major currencies, and list supported currency codes from a terminal workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live currency lookups send requested currency pairs to an external Frankfurter API endpoint.

Mitigation: Use only when live network exchange-rate queries are acceptable for the workflow; avoid this skill for offline-only or sensitive currency-query use cases.

Risk: Exchange-rate data depends on the external API being available and current.

Mitigation: Review returned dates and handle network or unsupported-currency errors before relying on conversion output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/fx-converter)
- [Frankfurter API](https://www.frankfurter.app/)
- [Frankfurter latest rates endpoint](https://api.frankfurter.app/latest)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Terminal text output with currency rates, converted amounts, supported-currency lists, and error guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, python3, and live network access to Frankfurter for exchange-rate data.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
