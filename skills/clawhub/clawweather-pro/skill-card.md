## Description:

Weather and forecasts via wttr.in and Open-Meteo, with multi-city comparison, 7-day planning, and an optional paid x402 trading-weather call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare weather across cities, plan travel around a 7-day forecast, and check trading-hub weather. The premium path is intended for conscious paid use with an X402_API_KEY.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The premium trading-weather path can send X402_API_KEY, a spending-capable payment credential, to an external or environment-selected endpoint.

Mitigation: Use the premium script only after reviewing the endpoint, keep X402_API_KEY scoped and secret, and avoid setting X402_BASE unless the destination is fully trusted.

Risk: Enabling HTTP for the premium endpoint can expose the API key in transit.

Mitigation: Keep the default HTTPS behavior and do not set X402_ALLOW_HTTP except in a controlled test environment.

Risk: Free weather scripts send city or hub choices to third-party weather services, which can reveal location interests or travel plans.

Mitigation: Avoid entering sensitive locations and disclose that city and hub names are sent to wttr.in or Open-Meteo.

Risk: The premium path is paid per call and can incur charges.

Mitigation: Run premium commands only after explicit user confirmation and monitor API-key usage or spending limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/clawweather-pro)
- [Publisher profile](https://clawhub.ai/user/northcap-group)
- [wttr.in weather service](https://wttr.in)
- [Open-Meteo forecast API documentation](https://open-meteo.com/en/docs)
- [Configured premium x402 endpoint](https://186.240.156.169:8791)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown tables and summaries for free tools; JSON for the premium trading-weather response.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free paths call third-party weather services with city or hub names; premium calls may charge a spending-capable API key.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
