## Description: <br>
Identifies sandstorm source areas by combining low-NDVI vegetation deficit, bare-soil fraction, wind-speed threshold exceedance, and upwind trajectory weighting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental monitoring teams use this skill to run local sandstorm source-area analysis from a multiband GeoTIFF or synthetic test scene and review generated raster and JSON outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include credential-store reads and an embedded Earthdata password. <br>
Mitigation: Remove bundled secrets and review credential-handling files before installation or execution. <br>
Risk: Bundled helper modules include online geocoding and arbitrary download utilities. <br>
Mitigation: Run in a network-restricted environment unless network access is explicitly required and reviewed. <br>
Risk: Bundled helper modules can persist cache data under the user's home directory. <br>
Mitigation: Inspect or disable cache behavior before running on sensitive systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sandstorm-source-identification) <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance plus GeoTIFF raster outputs, JSON parameter files, JSON run manifests, and concise CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces emission_potential.tif, source_mask.tif, source_contribution.tif, sandstorm_params.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and CLI VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
