## Description: <br>
Models surface solar radiation from a DEM or synthetic terrain using solar geometry, terrain shading, and simplified atmospheric transmittance, then outputs a radiation raster and run statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial or energy analysts use this skill to estimate daily surface solar radiation over a bounding box or local DEM. It supports offline synthetic runs and local GeoTIFF inputs for GIS-oriented modeling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports a suspicious package because the main solar-radiation tool appears offline, but bundled network and credential-handling code is not clearly disclosed for this skill's stated purpose. <br>
Mitigation: Review before installing. Use only the documented main entrypoint with explicit --bbox or --input, and do not provide local secrets or API keys unless the publisher removes or clearly documents the bundled geocoding, downloader, and credential modules. <br>
Risk: The security guidance states that hardcoded Earthdata credentials are present. <br>
Mitigation: The publisher should remove and rotate those credentials before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-solar-radiation-modeling) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, GeoTIFF raster, Shell commands] <br>
**Output Format:** [GeoTIFF raster, JSON statistics and manifest, plus concise CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes solar_radiation.tif, radiation_stats.json, and output-manifest.json to the configured output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; entrypoint VERSION also 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
