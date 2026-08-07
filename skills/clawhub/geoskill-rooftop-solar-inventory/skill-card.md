## Description: <br>
Inventories building rooftop solar potential by estimating usable area, slope and aspect, shading, PV capacity, annual energy yield, economics, and building-level candidate rankings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and energy planners use this skill to run building-level rooftop PV feasibility analysis, rank candidate rooftops, and generate reviewable outputs for solar deployment planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public data downloads and unpinned Python dependencies can change analysis behavior over time. <br>
Mitigation: Use a dedicated Python environment, review or pin dependencies, and set explicit output and cache directories before installation or production use. <br>
Risk: Demo or fallback runs can use synthetic building inputs, which are not suitable for real feasibility decisions. <br>
Mitigation: Provide real building inputs for production feasibility work and verify dataset-manifest.json does not report synthetic inputs before relying on rankings. <br>
Risk: Generated manifests may include local output paths or data-source metadata. <br>
Mitigation: Review output-manifest.json before sharing results and remove sensitive local paths or metadata when needed. <br>
Risk: Results are indicative when DSM data is absent, shading is simplified, or structural and ownership constraints are not assessed. <br>
Mitigation: Use DSM inputs where available and require manual engineering, structural, ownership, and economic review before deployment decisions. <br>


## Reference(s): <br>
- [Solar panel defaults](references/solar_panel_defaults.json) <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/geoskill-rooftop-solar-inventory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with bash commands plus GeoJSON, CSV, JSON, GeoTIFF, and log files from the Python CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include candidate rankings, manifests, QA checks, and optional shading masks; shading output requires DSM input.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
