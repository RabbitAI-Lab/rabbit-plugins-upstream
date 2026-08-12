## Description: <br>
Models habitat suitability probability from environmental rasters with random forest or logistic regression and outputs suitability GeoTIFF plus model parameter JSON with cross-validated AUC. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local habitat suitability modeling from multi-band environmental rasters or synthetic inputs, then review suitability probabilities, variable contributions, cross-validated AUC, and a run manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports under-disclosed geocoding, download, credential helpers, and an embedded Earthdata password in bundled files. <br>
Mitigation: Review or remove unused vendored helpers such as credentials.py, _place.py, aoi.py, and safe_download.py before installation. <br>
Risk: The offline privacy claim may not hold if network-capable helpers are present or enabled. <br>
Mitigation: Use the skill only after confirming network-capable helpers are absent, disabled, or explicitly reviewed for the intended deployment. <br>
Risk: Dependencies are not pinned in requirements.txt. <br>
Mitigation: Prefer a release with pinned dependencies or pin and review dependency versions before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-habitat-suitability-modeling) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [VENDORED.txt](_geoskill_core/VENDORED.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated runtime artifacts include GeoTIFF, JSON, and a run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The advertised modeling workflow runs locally, but security evidence says bundled vendored helpers require review before installation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
