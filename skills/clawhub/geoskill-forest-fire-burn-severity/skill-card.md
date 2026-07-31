## Description: <br>
Compute forest fire burn severity from pre/post-fire NIR and SWIR imagery using differenced Normalized Burn Ratio (dNBR), then classify severity into unburned, low, moderate, and high categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to assess forest fire burn severity, map fire damage, and generate burn-severity reports from trusted local imagery or supported downloaded imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic download mode may use unsuitable or duplicated imagery, which can produce misleading burn-severity reports. <br>
Mitigation: Prefer trusted local pre-fire and post-fire NIR/SWIR bands for real analysis; if auto-download mode is used, validate that distinct, suitable bands were fetched before relying on the report. <br>
Risk: The skill can perform network data downloads to Microsoft Planetary Computer and cache data locally. <br>
Mitigation: Install and run it only in environments where those downloads and local caching are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-forest-fire-burn-severity) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Analysis, JSON, Text] <br>
**Output Format:** [HTML report, JSON report, JSON manifest, and terminal status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes report.html, burn-severity-report.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and script --version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
