## Description: <br>
Classifies rice, wheat, and maize from multi-temporal SAR backscatter time series using per-pixel time-series, statistical, and phenological features with Random Forest, then outputs a classification GeoTIFF, area statistics, and a confusion matrix JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local SAR crop classification workflows for rice, wheat, and maize over a WGS84 bounding box or input raster, including synthetic offline evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes undisclosed credential and network helper code, including hardcoded Earthdata credentials. <br>
Mitigation: Review before install; require the publisher to remove hardcoded credentials, narrow or remove unrelated helper modules, and document any network lookups and cache locations. <br>
Risk: Supported dependency versions are not pinned in the release evidence. <br>
Mitigation: Pin and test supported dependency versions before operational deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-crop-classification) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifacts include GeoTIFF and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs include crop_classification.tif, crop_area_stats.json, confusion_matrix.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG.md list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
