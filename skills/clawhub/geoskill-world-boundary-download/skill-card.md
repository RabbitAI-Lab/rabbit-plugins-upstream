## Description: <br>
Download global administrative boundary vector data (Shapefile / GeoJSON / GeoPackage / TopoJSON) for any country or multi-country region. Backed by geoBoundaries (CC BY 4.0, default) with GADM 4.1 and Natural Earth as fallbacks. Supports bbox clipping, multi-country merge, and a rich metadata API (year, source, license, area, vertex count). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial content teams use this skill to locate, inspect, and download administrative boundary data by country, ISO code, or bounding box. It is suited for generating map-ready boundary files, metadata summaries, and multi-country region extracts while preserving source and license details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed credential and geocoding utilities unrelated to the boundary-download workflow, including hardcoded Earthdata credentials. <br>
Mitigation: Review the package before installation, remove or clearly isolate the unrelated _geoskill_core modules, and remove and rotate the embedded credentials before use. <br>
Risk: Dependency specifications are not tightly pinned. <br>
Mitigation: Install in an isolated environment and pin or review dependency versions before using the skill in production workflows. <br>
Risk: The skill downloads third-party boundary datasets whose licensing differs by source. <br>
Mitigation: Prefer the default geoBoundaries source for commercial use and review source-specific attribution or non-commercial restrictions before using GADM or fallback data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-world-boundary-download) <br>
- [Data Sources](docs/DATA_SOURCES.md) <br>
- [Design Document](docs/DESIGN.md) <br>
- [geoBoundaries](https://www.geoboundaries.org/) <br>
- [GADM](https://gadm.org/) <br>
- [Natural Earth](https://www.naturalearthdata.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON status output, and generated geospatial files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce Shapefile ZIP, GeoJSON, GeoPackage, or TopoJSON outputs, plus metadata such as source, license, bbox, area, and feature counts.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
