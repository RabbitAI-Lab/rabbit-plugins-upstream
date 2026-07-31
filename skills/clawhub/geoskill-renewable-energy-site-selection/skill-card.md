## Description: <br>
Multi-criteria site selection for solar PV and wind projects using hard constraints and weighted suitability analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and renewable energy planners use this skill to screen solar PV or wind farm locations, compare development zones, estimate potential installed capacity, and apply geospatial constraints such as slope, land cover, water, and protected areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BBox/AOI and date-range queries may be sent to NASA POWER and the Planetary Computer during automatic data download. <br>
Mitigation: Prefer local raster inputs for sensitive projects and use automatic download only when sharing the query area and date range with those services is acceptable. <br>
Risk: Downloaded data and query metadata can persist in the output directory or cache. <br>
Mitigation: Set explicit cache and output directories, review generated manifests, and clean or protect stored data according to project policy. <br>
Risk: Unpinned dependencies can affect reproducibility in regulated or audited workflows. <br>
Mitigation: Pin package versions and validate the environment before use in regulated or reproducible settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-renewable-energy-site-selection) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Code, Shell commands, Configuration] <br>
**Output Format:** [GeoTIFF, GeoJSON, HTML, JSON manifest, and Markdown or shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces suitability.tif, candidate_sites.geojson, report.html, and output-manifest.json in the configured output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
