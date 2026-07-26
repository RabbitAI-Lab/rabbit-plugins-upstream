## Description: <br>
Multi-temporal image compositing from local GeoTIFF files with cloud masking and median, mean, maxNDVI, or minRed compositing methods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to create local GeoTIFF composites, apply cloud masks, and generate preview or QA outputs for Landsat and Sentinel-2 workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags under-disclosed network geocoding, remote fetch orchestration, and sibling-script execution despite local-only documentation. <br>
Mitigation: Review before installing; use only local composite and cloud-mask commands unless the networked from-place workflow is explicitly acceptable. <br>
Risk: Using from-place may send place names or AOIs to third-party geocoding services and create local cache/output artifacts. <br>
Mitigation: Disable or remove from-place and geoskill download/geocoding helpers for offline-only use, and review generated cache and output locations before running. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/image-composite) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; CLI execution writes GeoTIFF, PNG, and JSON artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local GeoTIFF inputs; optional QA JSON and from-place cache/output artifacts.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
