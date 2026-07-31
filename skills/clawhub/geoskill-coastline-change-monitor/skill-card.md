## Description: <br>
Multi-temporal shoreline change rate analysis that generates transects, computes Endpoint Rate (EPR) and Linear Regression Rate (LRR), and identifies erosion hotspots for coastline retreat/accretion monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and coastal monitoring teams use this skill to compare shoreline positions across years, compute shoreline change rates, and identify erosion-prone segments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can write reports, data files, downloaded imagery, and cache files to local paths. <br>
Mitigation: Set explicit output and cache directories and review generated files before using them in downstream workflows. <br>
Risk: BBox/date mode can contact Microsoft Planetary Computer and cache imagery locally. <br>
Mitigation: Use local shoreline files when network access is not intended, and only enable bbox/date downloads in environments approved for remote data access. <br>
Risk: Unpinned geospatial dependencies can change behavior across installations. <br>
Mitigation: Use a locked and scanned dependency set for production deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-coastline-change-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [CLI guidance plus generated GeoJSON, CSV, HTML, and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces shoreline, transect, change-rate, erosion-hotspot, report, and manifest files in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
