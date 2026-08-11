## Description:

Assists agents with local wind resource assessment from wind-speed time series, including per-pixel Weibull fitting, wind power density, height extrapolation, and annual energy yield estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and energy or geospatial analysts use this skill to run local wind-resource assessments for siting, resource surveying, and energy-yield estimation. The workflow supports local wind-speed GeoTIFF inputs and offline synthetic data generation for validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports undocumented auxiliary network geocoding and credential-handling code in the package.

Mitigation: Review before installation; remove, document, or isolate auxiliary modules and require explicit opt-in for any network behavior.

Risk: The security evidence reports hardcoded Earthdata credentials.

Mitigation: Delete hardcoded credentials, rotate any exposed secrets, and use environment-managed credentials instead.

Risk: The security evidence recommends dependency pinning.

Mitigation: Pin and review dependencies before deployment in shared or production environments.

## Reference(s):

- [Skill README](README.md)
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-wind-resource-assessment)

## Skill Output:

**Output Type(s):** [shell commands, guidance, configuration, files]

**Output Format:** [Markdown guidance with shell commands; generated artifacts include GeoTIFF and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces mean wind speed, wind power density, Weibull parameter rasters, parameter JSON, and an output manifest when executed.]

## Skill Version(s):

1.0.0 (source: server release metadata and CLI VERSION; artifact changelog/openai.yaml list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
