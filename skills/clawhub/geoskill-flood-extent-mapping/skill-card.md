## Description: <br>
Extracts flood extent from SAR backscatter imagery for change analysis, hazard detection, and assessment reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial operators use this skill to process SAR backscatter rasters or downloaded Sentinel-1 scenes and generate flood extent summaries for situational awareness and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode fetches Sentinel-1 data from Microsoft Planetary Computer and writes downloaded files locally. <br>
Mitigation: Use local --sar inputs or allow outbound downloads only in environments where the Planetary Computer workflow and local output directory are approved. <br>
Risk: Dependency versions are not pinned in requirements.txt. <br>
Mitigation: Pin and review geoskill-data-fetcher, numpy, and rasterio versions before deploying in stricter operational environments. <br>
Risk: The argument validator uses eval-based lookup internally. <br>
Mitigation: Replace the lookup with getattr before use in high-assurance or tightly restricted execution environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-flood-extent-mapping) <br>
- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/) <br>
- [Sentinel-1 GRD collection](https://planetarycomputer.microsoft.com/dataset/sentinel-1-grd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and generated JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include flood-report.json, report.html, and output-manifest.json; auto-download mode may also save a Sentinel-1 input scene under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
