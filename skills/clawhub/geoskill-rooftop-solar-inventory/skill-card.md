## Description: <br>
Inventory building rooftop solar potential by estimating available area, slope/aspect, shading, PV capacity, energy yield, and economic viability, then producing building-level candidate rankings for solar deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and solar planning teams use this skill to evaluate rooftop PV potential across building portfolios, rank candidate buildings, and generate feasibility-study outputs from footprints, DSM data, point clouds, or auto-downloaded public datasets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Geospatial dependencies are not pinned, which can affect reproducibility or package resolution. <br>
Mitigation: Install in a controlled environment and review or pin dependencies before operational use. <br>
Risk: AOI auto-download mode contacts Microsoft Planetary Computer and NASA POWER and records run details in output manifests. <br>
Mitigation: Use auto-download only when external data access is acceptable, and avoid sharing manifests that expose sensitive local paths or AOI details. <br>
Risk: Runs without DSM input assume flat roofs and mark results as low confidence. <br>
Mitigation: Use DSM or other validated elevation data for higher-confidence roof geometry and review QA warnings before acting on rankings. <br>
Risk: Economic and solar potential estimates are auxiliary analysis and do not assess structural suitability, roof loading, ownership, or project-specific costs. <br>
Mitigation: Treat results as screening outputs and require engineering, structural, and financial review before deployment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-rooftop-solar-inventory) <br>
- [Solar panel defaults](references/solar_panel_defaults.json) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, shell commands] <br>
**Output Format:** [CLI-generated GeoJSON, CSV, JSON manifests, optional GeoTIFF shading raster, and run log] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include building rankings, rooftop candidate geometry, request metadata, dataset inventory, output statistics, and QA warnings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
