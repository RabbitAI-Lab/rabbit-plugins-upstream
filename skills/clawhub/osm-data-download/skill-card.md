## Description: <br>
Downloads OpenStreetMap features via Overpass API by bounding box, tag filter, semantic preset, administrative place, or custom query, and produces GeoJSON, Shapefile, ZIP bundles, and optional QA summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to prepare OpenStreetMap extracts for mapping, GIS analysis, and repeatable data refresh workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requested locations, bounding boxes, tag filters, and raw Overpass queries may be sent to public OSM-related services. <br>
Mitigation: Avoid sensitive project names or locations unless using a local or private geocoding and Overpass setup. <br>
Risk: QA summaries, cache files, and generated geospatial outputs may contain location details or query metadata. <br>
Mitigation: Review generated files before sharing or publishing backups. <br>
Risk: Loose dependency constraints can allow newer dependency versions to change behavior. <br>
Mitigation: Install with pinned, current dependency versions in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/osm-data-download) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [OpenStreetMap](https://www.openstreetmap.org) <br>
- [Overpass API endpoint](https://overpass-api.de/api/interpreter) <br>
- [Skill details reference](references/details.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, code, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated files may include GeoJSON, Shapefile sidecars, ZIP bundles, and QA JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may contain OpenStreetMap-derived data and query metadata; attribution and downstream data-license obligations remain with the user.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
