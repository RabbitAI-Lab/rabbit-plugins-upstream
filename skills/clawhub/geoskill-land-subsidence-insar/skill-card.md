## Description: <br>
Analyze land subsidence from InSAR displacement data for change analysis, hazard detection, and assessment reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run land-subsidence analysis on InSAR displacement rasters, identify subsidence hotspots, and generate machine-readable and human-readable reports. Auto-downloaded Sentinel-1 GRD data should be treated as an exploratory proxy rather than a vetted displacement product. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode can use Sentinel-1 GRD backscatter or intensity as a proxy for InSAR displacement, which may mislead hazard assessment. <br>
Mitigation: Use vetted displacement rasters for real subsidence decisions and treat GRD auto-download results as exploratory only. <br>
Risk: Unpinned runtime dependencies can create deployment uncertainty in controlled environments. <br>
Mitigation: Pin and review dependencies before deployment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; runtime outputs JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces subsidence-report.json, report.html, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
