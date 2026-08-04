## Description: <br>
Identify potential debris-flow gullies, integrate terrain, material source, rainfall trigger, and downstream exposure to produce basin-level hazard screening and risk assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and hazard-screening teams use this skill to run basin-level debris-flow screening, estimate runout zones, and produce reviewable GIS/report outputs for early assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may appear to be real site-specific debris-flow assessments while the security review states that the pipeline uses synthetic terrain, outlet, and infrastructure data. <br>
Mitigation: Treat outputs as screening or demonstration evidence only until real DEM, outlet, and infrastructure ingestion is implemented, verified, and clearly labeled. <br>
Risk: Optional data download and cache behavior can pull remote DEM assets and introduce dependency or data-source risk in production or sensitive environments. <br>
Mitigation: Review the download/cache behavior, pin dependencies, and validate data provenance before deployment. <br>


## Reference(s): <br>
- [Debris Flow Factors](references/debris_flow_factors.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-debris-flow-risk) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated artifacts include GeoJSON, raster or NumPy hazard output, CSV exposure inventory, HTML report, JSON manifests, QA data, and logs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are screening-level and should be reviewed before use in safety, planning, engineering, or emergency decisions.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
