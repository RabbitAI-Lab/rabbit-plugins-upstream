## Description: <br>
Estimates cumulative biomass from NDVI time-series integration with climate correction to yield a productivity index. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and agricultural analysts use this skill to compute farmland productivity rasters from local or synthetic NDVI time series and climate anomaly parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is flagged as suspicious because local farmland analysis is bundled with under-disclosed credential, geocoding, download, and cache code. <br>
Mitigation: Review the package before installation, run it in an isolated environment, and avoid placing real credentials in user-level secrets or netrc files unless the package is cleaned up and documented. <br>
Risk: Advertised offline behavior may not cover bundled helper code that can use network access or disk caching. <br>
Mitigation: Prefer local input or synthetic mode for untrusted runs and restrict network egress unless the network behavior is explicitly reviewed. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [SKILL](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-farmland-productivity) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoTIFF raster files, JSON run manifest, and concise console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces productivity_index.tif, ndvi_integral.tif, productivity_grade.tif, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
