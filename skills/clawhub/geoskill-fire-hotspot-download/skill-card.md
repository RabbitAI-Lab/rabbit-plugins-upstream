## Description: <br>
Downloads NASA FIRMS MODIS and VIIRS active fire hotspot data filtered by date, bounding box, place or preset, instrument, product, and confidence, with CSV or GeoJSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, environmental analysts, and fire monitoring teams use this skill to fetch active fire hotspot records for a chosen area and time window from NASA FIRMS. Agents can use it to prepare repeatable download commands, configure credentials, and produce geospatial files for downstream mapping or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a NASA FIRMS API key and can store it in a local configuration file. <br>
Mitigation: Prefer the FIRMS_API_KEY environment variable or a protected local config file, avoid passing real keys on the command line, and keep credential files out of shared workspaces. <br>
Risk: Verbose mode can expose request details while troubleshooting API calls. <br>
Mitigation: Do not use --verbose with real keys or in logs that may be shared. <br>
Risk: The security evidence flags dependency risk for review before installation. <br>
Mitigation: Pin or audit dependencies before use in production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-fire-hotspot-download) <br>
- [NASA FIRMS API documentation](https://firms.modaps.eosdis.nasa.gov/api/) <br>
- [NASA FIRMS MAP_KEY registration](https://firms.modaps.eosdis.nasa.gov/api/map_key/) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, code, files, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; runtime outputs are CSV, GeoJSON, or QA JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a NASA FIRMS API key. Queries send the key, bounding box, date range, and instrument selection to NASA FIRMS; downloaded records are processed locally.] <br>

## Skill Version(s): <br>
4.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
