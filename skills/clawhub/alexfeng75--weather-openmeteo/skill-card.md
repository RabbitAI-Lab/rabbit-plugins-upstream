## Description:

Get current weather and forecasts using Open-Meteo API (no API key required). Optimized for PowerShell environments with Chinese support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexfeng75](https://clawhub.ai/user/alexfeng75)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to query current weather and seven-day forecasts through Open-Meteo in PowerShell-oriented workflows, especially for Chinese city examples and bilingual output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The inspected package includes documentation that refers to PowerShell scripts, but the actual .ps1 files were not included.

Mitigation: Verify any PowerShell scripts from a trusted source before running them, and confirm they match the documented weather behavior.

Risk: The documentation suggests a persistent PowerShell execution-policy change.

Mitigation: Avoid running Set-ExecutionPolicy unless the security tradeoff is understood and accepted; prefer direct API requests when scripts are not needed.

Risk: Weather queries send requested coordinates and timezone to Open-Meteo.

Mitigation: Use only location data appropriate to share with the external weather service.

## Reference(s):

- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast)
- [Weather Open-Meteo on ClawHub](https://clawhub.ai/alexfeng75/skills/weather-openmeteo)
- [alexfeng75 Publisher Profile](https://clawhub.ai/user/alexfeng75)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with PowerShell command examples and plain-text weather output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries contact Open-Meteo with requested location coordinates and timezone; no API key is required.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
