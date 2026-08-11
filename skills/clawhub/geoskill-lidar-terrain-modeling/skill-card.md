## Description: <br>
Rasterizes DEMs from LiDAR point clouds with IDW or TIN interpolation and derives slope, aspect, raster outputs, and terrain statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS or remote-sensing practitioners use this skill to convert local or synthetic LiDAR point clouds into DEM, slope, and aspect products with run metadata for terrain analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports under-disclosed credential helpers that are not needed for the documented offline terrain workflow. <br>
Mitigation: Run only in an isolated environment with no production credentials, or require a stripped package with credential behavior removed or clearly documented before deployment. <br>
Risk: The security review reports network geocoding, download, and persistence helpers that do not fit the advertised offline purpose. <br>
Mitigation: Use local-input or synthetic workflows with outbound network access blocked unless the extra network behavior has been reviewed and approved. <br>
Risk: The authoritative security verdict is suspicious for this release. <br>
Mitigation: Perform security review and ask the publisher to explain or remove the unrelated helper behavior before commercial rollout. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-terrain-modeling) <br>
- [README](README.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [License](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Text] <br>
**Output Format:** [GeoTIFF rasters, JSON manifest/statistics files, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local outputs include DEM, slope, and aspect rasters plus terrain_stats.json and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact script VERSION also reports 1.0.0, while CHANGELOG.md and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
