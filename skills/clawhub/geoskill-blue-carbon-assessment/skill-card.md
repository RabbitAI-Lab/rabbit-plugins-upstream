## Description: <br>
Blue carbon ecosystem assessment that identifies mangrove, salt marsh, and seagrass ecosystems and estimates carbon stocks, changes, and uncertainty using IPCC default factors or project-specific data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and coastal project teams use this skill to run screening-level blue carbon assessments for mangrove, salt marsh, and seagrass ecosystems, including stock estimates, change analysis, uncertainty summaries, and field-sampling plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File-based assessment output may be generated from synthetic data when real raster loading is not fully implemented. <br>
Mitigation: Treat results as screening outputs, verify generated request and QA metadata before use, and require real raster loading or fail-closed behavior before relying on --ecosystem-raster results. <br>
Risk: Remote data-download behavior may affect data provenance and local cache handling if enabled. <br>
Mitigation: Confirm the contacted service, cache location, and cache-clearing process before enabling remote downloads in an operational workflow. <br>


## Reference(s): <br>
- [Blue Carbon Factors](references/blue_carbon_factors.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-blue-carbon-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with CLI commands and generated assessment files, including HTML, CSV, GeoJSON, JSON, and NumPy arrays.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs depend on ecosystem raster availability, carbon factor inputs, soil depth, years, and output directory.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
