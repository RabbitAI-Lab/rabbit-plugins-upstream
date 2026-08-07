## Description: <br>
Coastal flood risk assessment using static bathtub inundation with ocean connectivity, sea level rise and storm surge scenarios, exposure estimates, and adaptation priority zones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and coastal planning analysts use this skill to run coastal flood scenario assessments, compare water levels, inspect exposure outputs, and identify adaptation priority zones. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Python geospatial dependencies and optional remote DEM downloads may affect installation, runtime behavior, and data-source trust. <br>
Mitigation: Install in a controlled environment, review configured inputs and downloads, and use pinned dependencies or vetted data sources for operational runs. <br>
Risk: Exposure statistics may be demo or placeholder values when real population, building, road, and facility layers are not supplied. <br>
Mitigation: Validate exposure outputs against authoritative local asset datasets before using results for planning or safety decisions. <br>
Risk: The model is a static bathtub inundation estimate, not a hydrodynamic storm surge simulation, and results depend on vertical datum and defense assumptions. <br>
Mitigation: Confirm DEM and water levels share the same vertical datum, document defense assumptions, and treat outputs as screening estimates unless reviewed by qualified flood-risk specialists. <br>


## Reference(s): <br>
- [Flood scenarios configuration](references/flood_scenarios.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Analysis, Files, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and generated files including HTML, GeoJSON, CSV, NumPy, and JSON outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include report, exposure table, priority zones, request metadata, dataset manifest, output manifest, and QA checks.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
