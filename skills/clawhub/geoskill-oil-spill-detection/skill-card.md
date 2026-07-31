## Description: <br>
Detects likely oil-film candidates from SAR dark spots by combining backscatter segmentation, shape and texture features, wind cues, ship proximity, and natural slick indicators for human review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and response teams use this skill to run SAR oil-spill candidate detection workflows, rank suspicious dark spots, and generate review artifacts. The outputs support triage and evidence gathering, not final administrative, engineering, safety, or incident-causation decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outbound satellite data downloads and local caching may create data governance, network, or reproducibility concerns. <br>
Mitigation: Before installation or use, confirm that Microsoft Planetary Computer downloads, the selected cache directory, and dependency versions are acceptable for the operating environment; use a controlled environment and pinned dependencies when reproducibility or compliance matters. <br>
Risk: SAR dark spots can be caused by low wind, rain cells, internal waves, coastal streaks, or other natural slick indicators rather than oil. <br>
Mitigation: Treat candidates as review targets, use the generated confidence scores and QA files for triage, and require human review before drawing operational or incident-causation conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-oil-spill-detection) <br>
- [oil_spill_factors.json](references/oil_spill_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON, GeoTIFF or NumPy raster, CSV, JSON manifests, and PDF or text review reports, with Markdown CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include confidence scores, candidate geometries, feature tables, QA checks, request metadata, dataset and output manifests, and pending human-review status.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
