## Description:

Helps agents choose TomTom traffic endpoints, form requests, and explain incidents, traffic flow, tiles, viewport data, and road-segment results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simonjohnedwards-hub](https://clawhub.ai/user/simonjohnedwards-hub)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select TomTom traffic APIs, prepare incident or flow requests, and summarize returned traffic information. Live lookups require a configured TomTom API key and a callable HTTP tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TomTom API keys can be exposed if raw request URLs are shared.

Mitigation: Configure the key in the agent environment and redact it from any shared URLs or logs.

Risk: Traffic answers may be mistaken for live results when API access is unavailable.

Mitigation: Confirm the HTTP tool and API key before a live lookup; clearly state when live traffic cannot be queried.

## Reference(s):

- [TomTom Traffic API skill release](https://clawhub.ai/simonjohnedwards-hub/skills/tomtom-traffic-api)
- [Bundled TomTom Traffic API reference](artifact/references/tomtom-traffic-api.md)

## Skill Output:

**Output Type(s):** [Guidance, API request examples, Text]

**Output Format:** [Markdown or plain-language text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries include available location, delay, speed, severity, or closure details; no live result is claimed without API access.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
