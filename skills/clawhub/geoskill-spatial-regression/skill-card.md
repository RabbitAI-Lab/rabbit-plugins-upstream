## Description: <br>
Performs an end-to-end spatial regression workflow with OLS fitting, residual spatial-autocorrelation diagnostics, and SLM/SEM maximum-likelihood estimation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local spatial regression diagnostics and compare OLS, spatial lag, and spatial error models on synthetic or local input data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is advertised as offline spatial regression but includes helper modules for network geocoding, downloads, and home-directory caching. <br>
Mitigation: Review, remove, or clearly gate those bundled helper capabilities before deployment; run with network egress blocked when offline operation is required. <br>
Risk: Bundled credential-handling code can discover local API keys and includes hardcoded Earthdata fallback credentials. <br>
Mitigation: Remove fallback credentials, audit the credential helper, and provide secrets only through approved, explicit runtime configuration. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-regression) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Code] <br>
**Output Format:** [Markdown guidance plus JSON, GeoJSON, or GeoTIFF run artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces regression_stats.json and output-manifest.json; synthetic mode can run offline.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and geoskill-spatial-regression.py VERSION; artifact changelog and openai.yaml report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
