## Description: <br>
Coastal flood risk assessment using static bathtub inundation with ocean connectivity; it simulates sea level rise and storm surge scenarios, assesses population, building, and infrastructure exposure, and identifies adaptation priority zones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and coastal-planning analysts use this skill to run file-based or synthetic coastal flood exposure assessments, compare sea level rise and storm surge scenarios, and generate planning-oriented risk outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Synthetic exposure outputs may be mistaken for authoritative flood-planning results. <br>
Mitigation: Label synthetic and file-based runs as exploratory unless real DEM, exposure, defense, and ancillary layers are provided and independently verified. <br>
Risk: Static bathtub inundation can overstate or mischaracterize flooding because it does not model hydrodynamics, drainage, waves, or tidal dynamics. <br>
Mitigation: Describe results as static inundation estimates and require qualified review before using them for planning or emergency-management decisions. <br>
Risk: Remote-download mode and the default cache location may be unsuitable for private or restricted environments. <br>
Mitigation: Review data-source behavior and cache paths before execution, and configure a controlled cache directory when needed. <br>
Risk: Unpinned dependencies can reduce reproducibility. <br>
Mitigation: Pin dependency versions in deployment environments before repeatable or audited runs. <br>


## Reference(s): <br>
- [Flood scenario parameters](references/flood_scenarios.json) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance plus generated HTML, GeoJSON, CSV, NPY, JSON manifests, QA JSON, and run logs from the CLI tool.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may be synthetic-derived when no DEM or ancillary layers are provided; users should qualify results accordingly.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
