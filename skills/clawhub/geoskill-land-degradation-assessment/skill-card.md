## Description: <br>
Assesses SDG 15.3.1 land degradation using productivity trends, land use/land cover change, and soil organic carbon, classifying areas as degraded, stable, or improved. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental assessment teams use this skill to run local land-degradation analyses for a WGS84 bounding box or a multiband NDVI GeoTIFF. It produces geospatial rasters, SDG summary statistics, and a run manifest for review or downstream workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper code includes hardcoded Earthdata credentials and can read local credential stores if invoked. <br>
Mitigation: Remove hardcoded credentials, rely on explicit user-provided secrets, and run or install the package only in an isolated environment until this is remediated. <br>
Risk: The main command is described as offline, but bundled geocoding and downloader helpers add network-capable behavior that may surprise users. <br>
Mitigation: Delete unused network helpers or clearly document and gate any network-capable paths before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-land-degradation-assessment) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Release changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, GeoTIFF, JSON] <br>
**Output Format:** [GeoTIFF rasters plus JSON report and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes degradation.tif, productivity_slope.tif, sdg_report.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
