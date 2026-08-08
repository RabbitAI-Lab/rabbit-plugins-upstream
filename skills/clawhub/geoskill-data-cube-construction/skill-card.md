## Description: <br>
Builds coordinate-aware xarray/NetCDF remote-sensing data cubes from local GeoTIFF input or offline synthetic imagery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to construct multi-temporal, multi-band raster data cubes for local remote-sensing workflows, offline testing, and downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network, downloader, and credential-handling modules alongside the local data-cube command. <br>
Mitigation: Review the skill before use in sensitive environments and prefer a version that removes or clearly gates those modules. <br>
Risk: Dependencies are not pinned, which can change behavior across installations. <br>
Mitigation: Install in an isolated environment and pin reviewed dependency versions before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-data-cube-construction) <br>
- [README](README.md) <br>
- [SKILL](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [NetCDF data cube, JSON metadata and manifest files, and concise console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary generated files are data_cube.nc, cube_metadata.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and CLI constant; artifact changelog/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
