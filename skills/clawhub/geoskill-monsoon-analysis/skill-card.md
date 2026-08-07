## Description:

Analyzes monsoon systems by computing seasonal wind reversal, monsoon index, precipitation concentration, and monsoon onset and retreat dates for East Asia and South Asia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, climate analysts, and geospatial practitioners use this skill to run local monsoon diagnostics from wind-field and precipitation time series, including synthetic offline inputs or local GeoTIFF wind data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags under-disclosed credential, network, provenance, and data-integrity issues that need review before sensitive installation.

Mitigation: Review the package before installation, remove or clearly disclose unused credential and network helpers, remove hardcoded credentials, fix vendored provenance metadata, and pin dependencies.

Risk: Security guidance warns that real-input mode may produce real-looking precipitation metrics from synthetic placeholder precipitation.

Mitigation: Clearly label synthetic or placeholder precipitation outputs and avoid using those metrics for operational decisions unless validated against real precipitation inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-monsoon-analysis)
- [Publisher profile](https://clawhub.ai/user/ruiduobao)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON]

**Output Format:** [GeoTIFF rasters, JSON diagnostics, JSON run manifest, and optional console text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces monsoon_index.tif, u_wind_seasonal.tif, monsoon_diagnosis.json, and output-manifest.json in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
