## Description: <br>
Render 3D terrain from DEM and imagery with vertical exaggeration and an HTML viewer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to turn local DEM inputs or synthetic terrain into shaded 3D terrain visualizations and supporting raster and metadata outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security review reports under-disclosed credential and network helper code outside the advertised offline terrain renderer. <br>
Mitigation: Run only the documented main terrain script in an isolated environment, and avoid placing unrelated secrets in ~/.netrc or ~/.geoskill/secrets.json when using the skill. <br>
Risk: Remote geocoding and download helpers may make network calls if invoked. <br>
Mitigation: Prefer local GeoTIFF inputs or synthetic mode, and restrict network egress unless remote geocoding or download behavior is explicitly needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-3d-terrain-visualization) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, code, shell commands, configuration, guidance] <br>
**Output Format:** [HTML viewer, GeoTIFF raster, JSON metadata, and run manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs are terrain_3d.html, shaded_relief.tif, terrain_3d.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
