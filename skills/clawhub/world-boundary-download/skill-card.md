## Description: <br>
Download global administrative boundary vector data in Shapefile, GeoJSON, GeoPackage, or TopoJSON formats for countries and multi-country regions, with metadata and source/license details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and GIS/data engineers use this skill to locate, download, merge, clip, and inspect administrative boundary datasets for mapping and geospatial workflows. It is useful when an agent needs repeatable CLI commands and metadata-aware guidance for boundary data acquisition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency and supply-chain review is needed before installation, especially for the unexplained core package identified in security guidance. <br>
Mitigation: Install in a locked, isolated environment with vetted package versions and review requirements.txt before deployment. <br>
Risk: Normal use downloads boundary data from third-party services and stores a local cache. <br>
Mitigation: Use approved network egress, review source licenses for the selected dataset, and clear or relocate the cache when local retention is not desired. <br>
Risk: Included helper code for place-name geocoding may send location queries to third-party services and maintain a separate local cache. <br>
Mitigation: Avoid helper geocoding for sensitive locations, prefer explicit ISO/bbox inputs, and disable or clear the helper cache where privacy requirements apply. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/world-boundary-download) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Data sources](docs/DATA_SOURCES.md) <br>
- [Design document](docs/DESIGN.md) <br>
- [geoBoundaries](https://www.geoboundaries.org/) <br>
- [GADM](https://gadm.org/) <br>
- [Natural Earth](https://www.naturalearthdata.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON output examples; generated CLI runs may write Shapefile ZIP, GeoJSON, GeoPackage, TopoJSON, and metadata files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on selected country, administrative level, data source, format, bbox, and cache settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
