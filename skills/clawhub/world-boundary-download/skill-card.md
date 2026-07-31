## Description: <br>
Download global administrative boundary vector data (Shapefile / GeoJSON / GeoPackage / TopoJSON) for any country or multi-country region. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and mapping teams use this skill to download country and regional administrative boundary files, inspect metadata, clip by bounding box, merge multi-country regions, and choose among Shapefile, GeoJSON, GeoPackage, and TopoJSON outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential-management code can read local secret stores and includes a hardcoded Earthdata password fallback. <br>
Mitigation: Review or remove the credential helper before installation, and run the skill in an environment where it cannot access sensitive local credentials. <br>
Risk: The skill downloads boundary data from external network sources and writes output files plus cache entries. <br>
Mitigation: Restrict execution to approved network destinations and output directories, and clear or isolate the cache when processing sensitive workflows. <br>
Risk: Downloaded data may carry separate source-specific license obligations, including attribution for geoBoundaries and non-commercial limits for GADM. <br>
Mitigation: Prefer the default geoBoundaries source for commercial use, preserve attribution metadata, and use GADM only when its non-commercial terms fit the use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/world-boundary-download) <br>
- [Data Sources](docs/DATA_SOURCES.md) <br>
- [Design Document](docs/DESIGN.md) <br>
- [geoBoundaries](https://www.geoboundaries.org/) <br>
- [GADM](https://gadm.org/) <br>
- [Natural Earth](https://www.naturalearthdata.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON metadata, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands plus generated vector data files and JSON status or metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Shapefile zip, GeoJSON, GeoPackage, TopoJSON, cache state, and source/license metadata for downloaded boundary data.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
