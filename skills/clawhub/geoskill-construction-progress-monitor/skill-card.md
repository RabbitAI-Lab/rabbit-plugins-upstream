## Description: <br>
Monitors construction progress from multi-temporal satellite imagery by classifying project stages with spectral indices and detecting stagnation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, construction auditors, and infrastructure analysts use this skill to generate progress status files and stagnation reports from project boundaries, monitoring periods, schedules, and optional Sentinel-2 area-of-interest downloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Progress reports may appear imagery-based even when the main workflow simulates stage changes. <br>
Mitigation: Review outputs before operational use and require implementation changes or explicit demo labeling before treating results as real satellite-derived construction evidence. <br>
Risk: BBox or AOI download mode can query Microsoft Planetary Computer and cache downloaded imagery locally. <br>
Mitigation: Use bbox or AOI download mode only where external data access and local cache locations are approved; prefer reviewed local imagery in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-construction-progress-monitor) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Construction progress monitor script](artifact/scripts/construction_progress_monitor.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with CLI commands and generated geospatial output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write project_status.geojson, progress_timeseries.csv, stage_map.tif when rasterio is available, exceptions.csv, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
