## Description: <br>
Identify potential debris-flow gullies, integrate terrain, material source, rainfall trigger, and downstream exposure to produce basin-level hazard screening and risk assessment. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to run screening-level debris-flow gully identification, hazard indexing, runout estimation, and exposure summaries for an area of interest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can look like a real debris-flow assessment workflow while using synthetic terrain data. <br>
Mitigation: Label synthetic or demo mode clearly and do not rely on outputs for planning, emergency, engineering, property, or safety decisions. <br>
Risk: The workflow may download remote DEM data that the current executable path does not actually analyze. <br>
Mitigation: Require explicit consent for downloads and validate that downloaded DEM, outlet, and infrastructure inputs are ingested before presenting results as real-site analysis. <br>
Risk: Screening-level geometric runout and regional rainfall assumptions can misstate site-specific debris-flow risk. <br>
Mitigation: Use qualified review and dynamic engineering models before applying results to design, permitting, or risk management decisions. <br>


## Reference(s): <br>
- [debris_flow_factors.json](references/debris_flow_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Configuration] <br>
**Output Format:** [GeoJSON, GeoTIFF or NumPy raster, CSV, HTML, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include request metadata, dataset manifest, output manifest, and QA JSON; hazard output falls back to NumPy when rasterio is unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
