## Description:

pitstop helps agents query Italian fuel-station prices and EV charging stations by municipality, province, brand, or coordinate using MIMIT, OpenStreetMap, and ISTAT data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use pitstop to find low-price Italian fuel stations, compare station prices by area or brand, and locate nearby EV chargers while carrying data freshness and tariff caveats into the answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions can run future unreviewed versions of the external pitstop-cli package.

Mitigation: Use a pinned reviewed version such as pitstop-cli==1.2.0 or run the CLI in an isolated environment when supply-chain control matters.

Risk: Fuel prices are daily open-data records, not live or intraday prices, and local caches may be stale.

Mitigation: Check and report freshness, coverage, and partial-result fields before presenting a station as the cheapest option.

Risk: EV charger results do not include per-station kWh tariffs and external tariff pages can fail or vary by membership and payment method.

Mitigation: Use the official tariff_info_url for charging-cost questions, report failed links, and avoid guessing charger prices.

Risk: Open fuel-price feeds can include outliers, unscreened prices, or suspect station coordinates.

Mitigation: Surface outlier, median_basis, unscreened-price, and coordinate_suspect indicators as confidence caveats in user-facing answers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galjos/skills/pitstop)
- [Publisher profile](https://clawhub.ai/user/galjos)
- [pitstop CLI homepage](https://github.com/galjos/pitstop-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON or GeoJSON CLI output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should surface navigation URLs, cache freshness, coverage, outlier warnings, partial-result errors, and official charger tariff handoff links when present.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
