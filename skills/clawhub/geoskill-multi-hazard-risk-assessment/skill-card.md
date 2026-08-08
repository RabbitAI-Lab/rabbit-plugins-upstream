## Description: <br>
Computes and zones a multi-hazard composite risk index from hazard, exposure, and vulnerability factors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and risk-assessment teams use this skill to run local raster-based multi-hazard analysis and produce composite risk maps, risk zones, run manifests, and processing parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security evidence flags under-disclosed network, download, and credential-handling code outside the stated offline risk-calculation purpose. <br>
Mitigation: Review the package before installing, pin dependencies, and remove or audit unused helper modules before deployment. <br>
Risk: Helper modules may read local credential profiles or use embedded fallback credentials. <br>
Mitigation: Run with least-privilege local credentials and inspect credential-related modules before using real data workflows. <br>
Risk: Online geocoding and download helpers may introduce network access when users expect offline processing. <br>
Mitigation: Use synthetic or local GeoTIFF inputs for offline runs and restrict network access unless online helpers are explicitly needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-multi-hazard-risk-assessment) <br>
- [README](artifact/README.md) <br>
- [SKILL](artifact/SKILL.md) <br>
- [CHANGELOG](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI examples plus generated GeoTIFF and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces risk_index.tif, risk_zones.tif, risk_params.json, and output-manifest.json for each run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact changelog and openai.yaml state 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
