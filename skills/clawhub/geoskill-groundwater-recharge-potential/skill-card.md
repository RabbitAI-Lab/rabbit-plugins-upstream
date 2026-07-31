## Description: <br>
Screens groundwater recharge potential by combining terrain, soil, geology, land cover, drainage density, and rainfall with AHP, weighted overlay, fuzzy aggregation, sensitivity analysis, and optional spatial validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, planners, hydrogeology analysts, and developers use this skill to identify higher groundwater recharge potential zones, compare factor-weight scenarios, and generate candidate recharge area maps for planning review. Results are screening-level and require human review before engineering, administrative, or legal decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Geospatial dependencies and optional public dataset downloads may be unsuitable in locked-down or reproducible environments. <br>
Mitigation: Install only in an environment approved for geospatial package installation and public data access; review or pin requirements before use. <br>
Risk: The documentation's auto-download example may not fully match the included script arguments. <br>
Mitigation: Verify the intended command and required raster inputs before running; prefer explicit input raster paths when reproducibility matters. <br>
Risk: Screening-level suitability outputs can be misleading if treated as confirmed groundwater volumes or well success predictions. <br>
Mitigation: Use outputs for planning reference only and require hydrogeological, engineering, administrative, and legal review before decisions. <br>


## Reference(s): <br>
- [Default recharge factor scoring tables](references/recharge_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated geospatial artifacts such as GeoTIFF, GeoJSON, JSON manifests, logs, and an HTML report saved with a PDF filename] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces screening-level suitability outputs, candidate recharge zones, factor weights, sensitivity summaries, QA records, request and output manifests, and run logs when executed with raster inputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
