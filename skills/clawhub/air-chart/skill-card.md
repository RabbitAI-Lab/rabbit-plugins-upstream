## Description:

Query global air-quality data (OpenAQ monitoring network) and render high-resolution SVG trend charts. Use when the user asks to "check/compare air quality in a city, PM2.5/PM10/ozone trends, or generate an air-quality chart". Supports single-city trends, multi-city comparison (up to 4 cities), multi-parameter charts, and multi-station snapshots; automatically prefers active government reference-grade stations, overlays WHO guideline lines, and aligns timestamps to station local time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qiakai](https://clawhub.ai/user/qiakai)

### License/Terms of Use:

MIT

## Use Case:

People seeking global air-quality trends and comparisons use this skill to retrieve OpenAQ monitoring data and generate SVG charts for selected cities, pollutants, time ranges, or active stations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional npx skills installer is unversioned.

Mitigation: If using that installer, review it and verify the package version before installation.

Risk: The security review was partial and noted an external API finding.

Mitigation: Review the scripts and OpenAQ API interaction before use when scan coverage or external service access matters.

Risk: The documented persistent setup stores the OpenAQ API key in a local config file.

Mitigation: Restrict access to the config file, or use the environment variable for ephemeral runs.

## Reference(s):

- [ClawHub air-chart release](https://clawhub.ai/qiakai/skills/air-chart)
- [OpenAQ Explorer registration](https://explore.openaq.org/register)
- [OpenAQ account and API key](https://explore.openaq.org/account)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [SVG chart file with a plain-text data summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts show pollutant concentrations over time, city comparisons, multiple pollutants, or station snapshots; summaries include measurement units.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
