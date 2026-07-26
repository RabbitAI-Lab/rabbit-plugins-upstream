## Description: <br>
Searches the Recreation Information Database for campgrounds, recreation areas, and federal recreation facilities near a supplied place name or latitude/longitude. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanrea](https://clawhub.ai/user/seanrea) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to discover federal campgrounds and recreation facilities near a destination, collect facility IDs and metadata, and optionally produce JSON for follow-on automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using --location sends the entered place name to OpenStreetMap Nominatim for geocoding. <br>
Mitigation: Use --lat and --lon for coordinate searches when the free-form destination should not be shared with Nominatim. <br>
Risk: RIDB searches send coordinates and the RIDB API key to ridb.recreation.gov. <br>
Mitigation: Avoid sensitive destinations when that data flow is unacceptable, and manage the RIDB API key as a secret. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seanrea/skills/ridb-search) <br>
- [RIDB Portal](https://ridb.recreation.gov) <br>
- [RIDB API key profile](https://ridb.recreation.gov/profile) <br>
- [recreation.gov](https://www.recreation.gov) <br>
- [RIDB API Notes](artifact/references/api-notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a RIDB API key; location-name searches call OpenStreetMap Nominatim before querying RIDB.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
