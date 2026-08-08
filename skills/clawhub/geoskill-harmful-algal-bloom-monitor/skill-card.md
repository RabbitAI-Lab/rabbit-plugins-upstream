## Description: <br>
Monitors harmful algal bloom extent, duration, and risk level from water-color remote-sensing reflectance using NDCI, FLH, BGI, and ARI indices with quality checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Environmental analysts, geospatial developers, and operations teams use this skill to run algal bloom screening workflows for lakes, reservoirs, and coastal waters, producing candidate events, area statistics, and alert reports for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce operational-looking bloom reports from synthetic data when real imagery ingestion is not verified. <br>
Mitigation: Confirm that real imagery was ingested and correctly labeled before using outputs, and do not rely on reports for environmental, safety, regulatory, or operational decisions without expert review. <br>
Risk: Area of interest and date-range parameters may trigger external data access. <br>
Mitigation: Review network use before providing sensitive AOI or date parameters. <br>
Risk: Unpinned dependencies can reduce reproducibility across installations. <br>
Mitigation: Pin dependency versions in deployment environments before release or operational use. <br>
Risk: Single-index bloom signals can be confused with turbidity, aquatic vegetation, shallow water, or local optical conditions. <br>
Mitigation: Use multiple indices, local threshold calibration, quality masks, and human expert review before drawing monitoring conclusions. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/geoskill-harmful-algal-bloom-monitor) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Bloom model parameters](artifact/references/bloom_models.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts include HTML, GeoJSON, CSV, NPY, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces alert reports, detected-event geometries, daily bloom-area statistics, bloom probability and duration rasters, request metadata, manifests, and QA metadata.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
