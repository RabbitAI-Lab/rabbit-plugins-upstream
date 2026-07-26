## Description: <br>
Multi-temporal change detection for satellite imagery using NDVI difference, image differencing, and Change Vector Analysis (CVA). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to compare two co-registered satellite GeoTIFF images, detect vegetation or land-cover change, and generate change masks and statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Under-disclosed network behavior may send location search terms, bounding boxes, dates, and scene filters to external geospatial services. <br>
Mitigation: Use the local detect and report commands for private workflows, avoid fetch and place-resolution features for sensitive locations, and require explicit documentation or opt-in before enabling network-backed features. <br>
Risk: The privacy text says no data leaves the machine, but the security evidence reports network fetching and geocoding behavior. <br>
Mitigation: Treat the current privacy claim as incomplete, review the skill before installation, and update public documentation to list network endpoints and stored outputs. <br>
Risk: The security guidance calls out a dependency issue around tqdm. <br>
Mitigation: Pin or tighten the tqdm dependency before deployment and review the resolved dependency set in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/change-detection) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Developer notes](DEV.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, code, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated runtime artifacts include GeoTIFF, GeoJSON, CSV, and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on command options and can include change magnitude rasters, binary masks, vector polygons, statistics reports, and QA sidecar files.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
