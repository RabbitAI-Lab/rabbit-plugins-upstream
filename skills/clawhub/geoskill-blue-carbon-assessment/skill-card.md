## Description: <br>
Blue carbon ecosystem assessment - identify mangrove, salt marsh, and seagrass ecosystems, estimate carbon stocks, changes, and uncertainty using IPCC default factors or project-specific data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and coastal project teams use this skill to run screening-level blue-carbon stock, change, uncertainty, and sampling-plan assessments for mangrove, salt marsh, and seagrass ecosystems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce apparently real blue-carbon results from synthetic data even when a user supplies a raster file. <br>
Mitigation: Use it only for demo or experimental screening until file-based raster loading is implemented and synthetic outputs are clearly labeled. <br>
Risk: Documented CLI examples and dependency behavior may not match implemented support. <br>
Mitigation: Fix unsupported CLI examples and pin or otherwise control dependencies before using outputs for planning, reporting, finance, regulatory work, or field decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-blue-carbon-assessment) <br>
- [Blue carbon factors](artifact/references/blue_carbon_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with CLI examples and generated files such as HTML, CSV, GeoJSON, JSON, and NumPy arrays] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include report.html, carbon_summary.csv, change.geojson, sampling_plan.geojson, request.json, dataset manifests, qa.json, and synthetic raster arrays.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
