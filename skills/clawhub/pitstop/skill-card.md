## Description:

pitstop helps agents answer Italy fuel-price and EV-charger questions using official MIMIT fuel data, OpenStreetMap Overpass charger data, and ISTAT comune coordinates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel or logistics agents use this skill to find inexpensive fuel stations in Italy, compare station prices by place, brand, fuel, or coordinates, and locate nearby EV chargers while surfacing data freshness and tariff limitations.

### Deployment Geography for Use:

Italy

## Known Risks and Mitigations:

Risk: The skill runs the pitstop-cli package from the Python package ecosystem, and install metadata allows versions greater than or equal to 1.1.1 rather than one pinned reviewed version.

Mitigation: Prefer a pinned reviewed package version when possible, and run it with ordinary user privileges and normal filesystem and network containment.

Risk: Fuel prices are daily open-data values rather than live or intraday prices, and some returned prices may be unscreened, outliers, or attached to suspect coordinates.

Mitigation: Surface freshness, quality, outlier, unscreened, and coordinate-suspect indicators in user-facing answers instead of presenting every result as equally reliable.

Risk: EV charger results depend on OpenStreetMap Overpass availability and do not return per-station kWh tariffs.

Mitigation: Handle charger error fields explicitly and direct users to the returned tariff information URL instead of guessing charger pricing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galjos/skills/pitstop)
- [pitstop-cli homepage](https://github.com/galjos/pitstop-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command examples and JSON or GeoJSON output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include navigation URLs, quality and outlier flags, and tariff information URLs for EV chargers; requires the pitstop binary.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
