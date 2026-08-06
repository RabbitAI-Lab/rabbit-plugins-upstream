## Description: <br>
Extracts pile IDs, coordinates, diameters, top elevations, and rock embedment calculations from pile foundation DXF drawings into Excel summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sxp1941](https://clawhub.ai/user/sxp1941) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and construction estimators use this skill to inspect pile foundation DXF files, extract pile parameters, calculate rock embedment depths from contour data, and prepare Excel summaries for quantity statistics, analysis, or bid tables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The interpolation script saves changes back to the specified Excel workbook. <br>
Mitigation: Run interpolation on a copy of important project workbooks and review the appended columns before relying on the results. <br>
Risk: DXF layer conventions, contour coverage, or pile-label matching can affect extracted coordinates, elevations, and embedment depths. <br>
Mitigation: Use the DXF analysis step first, confirm the detected layers and datum, and have an engineer review the generated Excel summary against the source drawing. <br>


## Reference(s): <br>
- [DXF pile drawing patterns](references/dxf_pile_patterns.md) <br>
- [ClawHub skill page](https://clawhub.ai/sxp1941/skills/dxf-pile-extraction) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown guidance with bash commands; generated Excel workbooks and annotated DXF files when scripts are run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Excel outputs include pile parameter and summary sheets; optional interpolation appends rock elevation and embedment-depth columns.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
