## Description: <br>
Multi-temporal shoreline change rate analysis that generates transects, computes Endpoint Rate (EPR) and Linear Regression Rate (LRR), and identifies erosion hotspots for coastline retreat or accretion monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and coastal monitoring teams use this skill to compare shoreline positions across years, compute transect-based change rates, and identify erosion-prone segments from vector shorelines or raster water masks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional bbox/date mode can contact Microsoft Planetary Computer and cache downloaded imagery. <br>
Mitigation: Require explicit approval for network mode and set controlled output and cache directories for enterprise or sensitive locations. <br>
Risk: Unpinned geospatial dependencies can change behavior across environments. <br>
Mitigation: Pin or lock dependencies before production use and verify outputs against known shoreline samples. <br>
Risk: Coastline change rates depend on input shoreline quality, coordinate reference system, and comparable observation dates. <br>
Mitigation: Validate source data, projection, and year mapping before relying on erosion hotspot outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-coastline-change-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated artifacts include GeoJSON, CSV, HTML, and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces shoreline, transect, change-rate, hotspot, report, and manifest outputs in the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
