## Description: <br>
Detects ships in single-polarization SAR intensity imagery with CA-CFAR or OS-CFAR detection and connected-component clustering, producing GeoJSON vectors and related detection outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to detect maritime vessel targets in local SAR imagery or synthetic SAR test data for surveillance, port traffic analysis, illegal fishing monitoring, and search-and-rescue screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed credential, geocoding, download, and cache helpers, including hardcoded Earthdata credentials. <br>
Mitigation: Review before installation, remove hardcoded credentials and unused helper modules, and confirm that any credential handling is explicit and environment-based. <br>
Risk: The skill is described as local or offline by default, but security guidance notes network geocoding and downloader helpers in the distribution. <br>
Mitigation: Disclose any network behavior, run in a restricted environment when evaluating, and remove helper code that is not required for SAR ship detection. <br>
Risk: Dependencies are unpinned, which can change runtime behavior over time. <br>
Mitigation: Pin and review dependencies before routine use or deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-ship-detection) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoJSON, GeoTIFF, JSON, and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ship centroids, detection masks, per-ship attributes, detection counts, and an output manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact changelog lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
