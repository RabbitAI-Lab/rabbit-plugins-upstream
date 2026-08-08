## Description: <br>
Computes coastal erosion and accretion volumes from two-epoch LiDAR point cloud or DSM differencing, extracts shorelines, and estimates retreat rates using the End Point Rate method. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and coastal-domain users can use this skill to run local coastal erosion analysis from LiDAR point clouds or synthetic DSM data and produce rates, volume estimates, and geospatial output files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Undisclosed credential and network helper code may expand the operational surface beyond the visible coastal-analysis CLI. <br>
Mitigation: Review before installation, remove or clearly gate unused credential/geocoding/download helpers, and require secrets to come from user-managed environment or secret files. <br>
Risk: Synthetic or modeled outputs may be mistaken for results from real two-period LiDAR observations. <br>
Mitigation: Clearly label synthetic or modeled outputs and require users to verify input epochs before relying on retreat rates or volume estimates. <br>
Risk: Unpinned dependencies and unclear vendored provenance can make deployment and review less reproducible. <br>
Mitigation: Pin and audit dependencies, and correct vendored provenance before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-coastal-erosion) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, files, configuration] <br>
**Output Format:** [Markdown guidance with shell commands; generated files include GeoTIFF, GeoJSON, JSON rates, and a JSON output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default; synthetic or modeled outputs should be clearly labeled before operational use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
