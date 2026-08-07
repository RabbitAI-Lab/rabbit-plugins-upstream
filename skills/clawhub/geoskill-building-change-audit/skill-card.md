## Description: <br>
Object-level building change detection between two epochs that identifies new, demolished, expanded, reduced, split, and merged buildings from footprint vectors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and audit teams use this skill to compare before and after building footprint datasets and generate object-level construction change reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode can ignore the requested date range or fall back to synthetic data, which can make audit results misleading for real temporal analysis. <br>
Mitigation: For real audits, provide trusted before and after building files and verify that output-manifest.json shows real downloaded inputs before relying on results. <br>
Risk: Building change classifications depend on input geometry quality, IoU threshold, and area tolerance. <br>
Mitigation: Validate source footprints and tune --match-iou and --area-tolerance against a reviewed sample before operational use. <br>
Risk: Dependency behavior can affect geospatial parsing, matching, and data download results. <br>
Mitigation: Pin and scan dependencies before use in sensitive environments. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoJSON, HTML report, JSON manifest, and concise CLI progress text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes building_changes.geojson, report.html, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
