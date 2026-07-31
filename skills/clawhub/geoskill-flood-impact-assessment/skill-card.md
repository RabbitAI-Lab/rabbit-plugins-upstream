## Description: <br>
Overlay flood extent with population, buildings, roads, and cropland to estimate affected objects and generate impact reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and emergency-response teams use this skill to run flood extent overlays against exposure data, estimate affected population and roads, and generate flood impact reports from local rasters or downloaded Sentinel-1 data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode synthesizes population data, which can make affected-population numbers look decision-ready when they are not real exposure estimates. <br>
Mitigation: Use a real population raster for operational assessments, or label and review synthetic-population outputs before sharing reports. <br>
Risk: The skill advertises building and cropland impact capabilities that are not implemented in the analyzed script. <br>
Mitigation: Do not use this release for building or cropland counts until those analyses are implemented and validated. <br>
Risk: The tool can download remote Sentinel-1 data and write reports and assets into an output directory. <br>
Mitigation: Run it in a controlled environment, review requested bounding boxes and date ranges, and direct outputs to an expected workspace path. <br>
Risk: Unpinned geospatial dependencies may change behavior across environments. <br>
Mitigation: Install in a pinned or locked environment before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-flood-impact-assessment) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated HTML report, JSON results, and JSON manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes report.html, impact-report.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
