## Description: <br>
Performs GCP-based polynomial geometric correction and outputs corrected imagery plus RMS error reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to correct distorted raster imagery with ground control points, inspect RMS residuals, and produce local GeoTIFF and JSON outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is described as a local geometric correction utility, but the authoritative security evidence says it also ships unrelated credential, downloader, geocoding, and hardcoded-password code. <br>
Mitigation: Review carefully before installing; remove or isolate unrelated network, downloader, and credential modules; delete and rotate hardcoded Earthdata credentials; and document any network or secret access before normal use. <br>
Risk: Incorrect GCPs, polynomial order, or bounding boxes can produce misleading corrected imagery. <br>
Mitigation: Validate inputs before use and inspect RMS totals, per-GCP residuals, and the output manifest before relying on corrected imagery. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-geometric-correction) <br>
- [README](README.md) <br>
- [Skill Instructions](SKILL.md) <br>
- [Synthetic CLI Evaluation Manifest](_test_cli_order1/output-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [GeoTIFF raster files, JSON RMS reports, JSON run manifests, and concise CLI status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs are corrected.tif, rms_report.json, and output-manifest.json; synthetic mode can run offline.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
