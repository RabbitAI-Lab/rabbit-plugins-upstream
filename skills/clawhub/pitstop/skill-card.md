## Description:

pitstop helps agents find Italian fuel-station prices and EV charging stations by municipality, province, brand, or coordinate using MIMIT, OpenStreetMap, and ISTAT data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use pitstop to answer Italy-specific fuel-price and EV-charger lookup questions, compare station options, and return compact JSON or GeoJSON results with caveats about data freshness and tariffs.

### Deployment Geography for Use:

Italy

## Known Risks and Mitigations:

Risk: The skill depends on a third-party CLI package and public data services for fuel and EV charger lookups.

Mitigation: Install only from the documented uvx or pipx package path and use the returned freshness, warning, and error fields when answering.

Risk: Returned fuel prices and EV charger information may be stale, incomplete, or estimated from open data.

Mitigation: Treat prices as estimates, surface stale-cache and partial-result warnings, and avoid presenting EV charging tariff amounts unless verified from the official tariff link.

Risk: Outlier prices, unscreened prices, or suspect station coordinates can mislead route or purchase decisions.

Mitigation: Check quality metadata, outlier flags, median basis, and coordinate warnings before recommending a station.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galjos/skills/pitstop)
- [pitstop-cli homepage](https://github.com/galjos/pitstop-cli)
- [Publisher profile](https://clawhub.ai/user/galjos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and JSON or GeoJSON output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should surface navigation URLs, stale-cache warnings, partial-result errors, outlier flags, coordinate concerns, and official EV tariff links when present.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
