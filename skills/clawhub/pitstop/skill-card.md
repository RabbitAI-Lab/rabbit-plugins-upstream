## Description: <br>
pitstop helps agents answer Italy-specific fuel price and EV charging questions using MIMIT fuel data, OpenStreetMap charger data, and ISTAT municipality coordinates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galjos](https://clawhub.ai/user/galjos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to find cheaper Italian fuel stations, compare fuel prices by place, brand, or coordinate, and locate nearby EV chargers with tariff caveats surfaced. <br>

### Deployment Geography for Use: <br>
Italy <br>

## Known Risks and Mitigations: <br>
Risk: Fuel prices and EV charger details may be stale or incomplete because the skill relies on public data sources and local caching. <br>
Mitigation: Surface freshness, tariff caveats, and official tariff links in user-facing answers instead of presenting results as live guarantees. <br>
Risk: Some returned fuel prices or station coordinates may be open-data errors or low-confidence values. <br>
Mitigation: Check quality fields, outlier flags, unscreened price status, and coordinate_suspect before recommending a station. <br>
Risk: The required third-party CLI makes public-data network requests and caches fuel or charger datasets locally. <br>
Mitigation: Install only in environments where that network and local caching behavior is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/galjos/skills/pitstop) <br>
- [Publisher profile](https://clawhub.ai/user/galjos) <br>
- [pitstop-cli source homepage](https://github.com/galjos/pitstop-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, GeoJSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or GeoJSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fuel station output includes stations, query, quality, navigation URLs, and price screening details; charger output may include Overpass error information and tariff information URLs.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
