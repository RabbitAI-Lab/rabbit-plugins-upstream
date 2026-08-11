## Description: <br>
Fuses NDVI, NDRE, and LST into a crop health score with historical anomaly detection and spatial clustering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and agricultural operators can use this skill to run local crop-health analysis over a WGS84 bounding box or a local multiband GeoTIFF. It produces vegetation, anomaly, health-score, classification, and clustering outputs for field-condition review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential helpers include hardcoded Earthdata credentials and related token-handling paths. <br>
Mitigation: Remove the hardcoded credentials, rotate any exposed account secrets, and require users to provide credentials through their own environment or secrets file. <br>
Risk: The package includes network and location-cache helpers that are not clearly described by the advertised local crop-health workflow. <br>
Mitigation: Document any geocoding, download, or cache behavior before deployment, and run the skill in synthetic or local-input mode when network access is not intended. <br>
Risk: Dependencies are unpinned, which can make scientific and geospatial outputs vary across environments. <br>
Mitigation: Pin and review numpy, rasterio, scipy, and clustering dependencies in a controlled environment before routine use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-health-diagnosis) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration] <br>
**Output Format:** [GeoTIFF rasters, JSON run manifest, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary runtime outputs include health_score.tif, diagnosis_layers.tif, health_level.tif, health_cluster.tif, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
