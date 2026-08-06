## Description: <br>
Downloads OpenStreetMap features through Overpass API by bounding box, tag filter, semantic preset, or administrative place name and writes GIS-ready local outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and data engineers use this skill to retrieve public OpenStreetMap features for mapping, QA, and downstream geospatial analysis. It supports bbox, tag, custom Overpass QL, and administrative-place workflows with GeoJSON, Shapefile, zip, and QA summary outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-specified place names, bounding boxes, and map queries are sent to public OSM, Nominatim, and Overpass services. <br>
Mitigation: Use reasonably scoped public geodata queries, avoid sensitive locations when that matters, or run against a trusted local Overpass or Nominatim service. <br>
Risk: The tool writes geodata outputs to user-selected local paths. <br>
Mitigation: Review output paths before execution and run in a workspace where generated GeoJSON, Shapefile, zip, and QA files are expected. <br>
Risk: Large or dense OSM queries can hit rate limits, timeouts, or excessive result sizes. <br>
Mitigation: Keep bounding boxes small, use rate delays and timeouts appropriate to the query, and split large areas into smaller requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-osm-data-download) <br>
- [Details reference](references/details.md) <br>
- [OpenStreetMap](https://www.openstreetmap.org) <br>
- [Overpass API endpoint](https://overpass-api.de/api/interpreter) <br>
- [Nominatim search endpoint](https://nominatim.openstreetmap.org/search) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Code, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples; runtime outputs include GeoJSON, ESRI Shapefile sidecars, zipped Shapefile bundles, and JSON QA summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public OSM, Nominatim, and Overpass services; output paths are user-specified and Shapefile attributes may be truncated.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
