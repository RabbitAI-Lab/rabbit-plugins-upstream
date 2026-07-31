## Description: <br>
Screens tailings dam bodies, reservoir areas, catchments, and downstream exposure using remote sensing change detection to produce patrol priorities based on hazard, exposure, and evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial risk teams use this skill to screen tailings dam facilities, compare remote-sensing evidence, estimate catchments and simplified downstream impact zones, and prioritize patrol or engineering review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network-enabled bbox or AOI analysis can disclose an area of interest and date range to external geospatial data services and can store downloaded data locally. <br>
Mitigation: Use local DEM and water-mask files for sensitive sites, control cache and output locations, and review data handling before running the skill. <br>
Risk: Dependency behavior may change in uncontrolled environments. <br>
Mitigation: Pin or lock dependencies before installing in controlled or production environments. <br>
Risk: The generated tailings dam risk outputs are screening aids and can be incomplete or misleading if input facility, DEM, water-mask, exposure, or deformation data is incomplete. <br>
Mitigation: Treat outputs as prioritization evidence only and require review by qualified engineers before making safety decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-tailings-dam-risk) <br>
- [risk_rules.json](references/risk_rules.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands and generated GeoJSON, CSV, HTML, JSON, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces screening artifacts such as facility change polygons, catchments, screening zones, downstream exposure tables, risk reports, manifests, QA output, and run logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
