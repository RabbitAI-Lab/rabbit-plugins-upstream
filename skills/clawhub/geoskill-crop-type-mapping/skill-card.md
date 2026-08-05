## Description: <br>
Provides a crop type mapping workflow for AOI and date inputs that generates crop classification, confidence, area, QA, and manifest outputs; release security evidence indicates the inspected code primarily uses synthetic scenes rather than operational imagery. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts can prototype crop classification workflows for a bounding box, AOI, year, or date range and review generated maps, statistics, manifests, and QA outputs. Treat results as demonstration output unless real imagery ingestion, provenance, and validation are confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users could mistake synthetic or demo crop mapping outputs for operational remote-sensing analysis. <br>
Mitigation: Label synthetic outputs clearly and require real imagery ingestion, explicit data provenance, and validation against ground truth before operational use. <br>
Risk: Use in planning, insurance, government, or other high-impact decisions could rely on unsupported accuracy claims. <br>
Mitigation: Restrict the release to demonstration use unless accuracy is measured on real data and reviewed for the intended geography and decision context. <br>
Risk: The skill describes optical/SAR crop mapping, but security guidance calls for SAR support to be removed or implemented. <br>
Mitigation: Align public claims with implemented sensor support before release, or document SAR as unsupported. <br>
Risk: Unpinned dependencies may change runtime behavior or reproducibility. <br>
Mitigation: Pin dependencies and record tested versions before relying on generated results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-type-mapping) <br>
- [Crop phenology reference schema](artifact/references/crop_phenology.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, Configuration] <br>
**Output Format:** [Markdown guidance with CLI examples plus generated GeoTIFF, GeoJSON, CSV, JSON, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include class rasters, confidence rasters, vector polygons, area statistics, request and dataset manifests, QA data, accuracy data, and run logs.] <br>

## Skill Version(s): <br>
2.0.0 (source: evidence.release.version; changelog: v2.0.0: rename displayName to English) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
