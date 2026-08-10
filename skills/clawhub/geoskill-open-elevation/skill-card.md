## Description: <br>
Query elevation data for latitude and longitude coordinates using the public Open-Elevation API, with single-point and batch CSV workflows and CSV or JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial practitioners use this skill to retrieve elevation values for individual coordinates or CSV batches without managing an API key. It is suited for agent-assisted geodata enrichment, QA summaries, and lightweight elevation lookup workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coordinates are sent to Open-Elevation, and place-name lookups send the place text to Nominatim. <br>
Mitigation: Avoid private or sensitive locations, prefer latitude and longitude inputs when possible, and review external API terms before managed use. <br>
Risk: The security scan notes that dependency constraints should be updated before use in managed or security-sensitive environments. <br>
Mitigation: Pin and review dependency versions, then rescan the installed environment before deployment. <br>
Risk: Public elevation data can vary by source, region, ocean coverage, and service rate limits. <br>
Mitigation: Validate outputs for the target region, keep batch chunks within documented limits, and cite the underlying data source for published results. <br>


## Reference(s): <br>
- [Open-Elevation](https://open-elevation.com/) <br>
- [Open-Elevation lookup endpoint](https://api.open-elevation.com/api/v1/lookup) <br>
- [Nominatim search endpoint](https://nominatim.openstreetmap.org/search) <br>
- [NASA Shuttle Radar Topography Mission](https://www2.jpl.nasa.gov/srtm/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, CSV files, JSON files] <br>
**Output Format:** [Plain text, CSV, or JSON from CLI lookup and batch commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-point lookup prints one CSV-style row or one JSON object; batch mode writes CSV or JSON result files with latitude, longitude, and elevation fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
