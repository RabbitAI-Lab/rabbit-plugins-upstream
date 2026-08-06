## Description: <br>
Predicts future groundwater levels from historical water-level time series and precipitation or abstraction drivers, then spatially interpolates predictions and reports uncertainty. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, hydrologists, and water-resource analysts use this skill to forecast groundwater levels, assess over-extraction warning signals, and generate regional prediction rasters from local or synthetic groundwater data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes undisclosed credential and network helper code, including a plaintext external-service password. <br>
Mitigation: Require the publisher to remove and rotate embedded credentials before installation or deployment. <br>
Risk: Network, download, and geocoding helper code is present even though the main workflow is described as mostly local. <br>
Mitigation: Use only the documented main script with explicit --bbox or local --input data, and review or remove unused network helper paths before deployment. <br>
Risk: Unpinned dependencies can change behavior or introduce supply-chain risk. <br>
Mitigation: Pin and review dependencies before production use. <br>
Risk: The tool may access local credential files if run in an environment that exposes them. <br>
Mitigation: Run tests in an isolated environment without personal credential files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-groundwater-level-prediction) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [License](artifact/LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Python CLI guidance and generated GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Typical files include predicted_level.tif, prediction_curve.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
