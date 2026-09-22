## Description:

pitstop helps agents query Italian fuel-station prices and EV charging stations by municipality, province, brand, or coordinates using MIMIT Osservaprezzi Carburanti, OpenStreetMap, and ISTAT data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use pitstop to answer Italy-focused fuel-price, fuel-station, and EV-charger lookup questions while preserving source freshness, quality, and tariff caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on running the pitstop CLI and allowing it to fetch and cache public fuel and charger data.

Mitigation: Install only in environments where that CLI dependency and data access are acceptable.

Risk: EV charger results do not provide per-station kWh tariffs.

Mitigation: Use the returned operator tariff link and avoid quoting charging prices unless verified from that source.

Risk: Fuel prices come from daily open data and may include stale, unscreened, outlier, or suspect-coordinate records.

Mitigation: Surface freshness, quality, outlier, and coordinate warnings from the tool output when answering users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galjos/skills/pitstop)
- [Project homepage](https://github.com/galjos/pitstop-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI command examples and JSON or GeoJSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should surface stale-cache, partial-result, outlier, coordinate, and charger-tariff caveats when present.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
