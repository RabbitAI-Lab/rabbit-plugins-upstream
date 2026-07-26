## Description: <br>
Download MODIS and VIIRS active fire hotspot data from NASA FIRMS with date, bounding-box, instrument, and output-format filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial workflows use this skill to fetch NASA FIRMS active-fire hotspot records for fire monitoring, air-quality studies, land management, and related spatial analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name lookup can contact third-party geocoding services, which may expose queried locations. <br>
Mitigation: Use explicit --bbox coordinates for sensitive work and review location inputs before running place-based queries. <br>
Risk: The skill stores or reads a FIRMS API key and writes generated datasets locally. <br>
Mitigation: Store the key through an environment secret manager where possible and keep generated datasets out of version control unless intentional. <br>
Risk: The security verdict is suspicious because documented network behavior does not fully match the place-name feature. <br>
Mitigation: Review the security summary before installation and constrain dependencies to patched versions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/fire-hotspot-download) <br>
- [NASA FIRMS API documentation](https://firms.modaps.eosdis.nasa.gov/api/) <br>
- [NASA FIRMS API key registration](https://firms.modaps.eosdis.nasa.gov/api/map_key/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with inline shell commands; the invoked script can write CSV or GeoJSON data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a NASA FIRMS API key and user-supplied spatial and temporal filters.] <br>

## Skill Version(s): <br>
0.3.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
