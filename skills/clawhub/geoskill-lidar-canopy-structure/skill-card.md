## Description: <br>
Extracts forest canopy structure parameters from LiDAR point clouds by generating DTM and CHM layers, detecting individual trees, and estimating tree height and crown attributes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and forestry teams use this skill to process local or synthetic LiDAR point clouds into canopy height, individual-tree, and summary analysis outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed geocoding, download, and credential-handling helpers despite an offline/no-network claim. <br>
Mitigation: Review or remove the unused geocoding, download, and credential modules before installation, especially credentials.py. <br>
Risk: Testing the full package in an unconstrained environment may allow behavior outside the documented local LiDAR workflow. <br>
Mitigation: Evaluate the skill in a constrained environment and treat the offline claim as unverified for the full package. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-canopy-structure) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifacts include GeoTIFF, GeoJSON, JSON statistics, and JSON run manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports synthetic data generation and local point-cloud inputs with CLI parameters for bounding box, cell size, minimum height, and output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
