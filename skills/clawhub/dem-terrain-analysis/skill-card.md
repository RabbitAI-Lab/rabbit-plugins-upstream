## Description: <br>
Generates terrain derivatives such as slope, aspect, hillshade, contours, curvature, hydrology layers, watershed, and viewshed from DEM GeoTIFF data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run a Python CLI that converts DEM GeoTIFF inputs into terrain-analysis rasters and contour GeoJSON for mapping, hydrology, and terrain review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-resolution options can involve network or download behavior that is under-disclosed by the skill. <br>
Mitigation: Treat from-place and --place as network-capable, review requested locations before use, and run the skill in an environment where network access is intentional. <br>
Risk: Hardcoded Earthdata credentials are reported in the security evidence. <br>
Mitigation: Do not rely on bundled credentials; the publisher should remove and rotate them, and users should provide their own secrets through approved secret management. <br>
Risk: Dynamic helper loading from local _shared/place_resolver.py can execute unexpected local code. <br>
Mitigation: Run the skill only from trusted working directories and avoid directories containing untrusted _shared helper files. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/dem-terrain-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated CLI outputs are GeoTIFF and GeoJSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes terrain derivative rasters and contour vectors to user-selected output paths.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
