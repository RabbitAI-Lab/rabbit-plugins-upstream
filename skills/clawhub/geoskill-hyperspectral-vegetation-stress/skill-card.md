## Description: <br>
Detects vegetation stress using red-edge indices NDRE, REP, and PRI plus spectral angle mapping, producing stress rasters and anomaly vectors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing teams use this skill to assess vegetation stress over a bounding box or local hyperspectral GeoTIFF. It supports synthetic offline runs for validation and local processing workflows for stress classification and anomaly extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper code includes credential, geocoding, download, and persistent-cache behavior that may be broader than the main local raster-analysis workflow. <br>
Mitigation: Review and scope the helper modules before deployment; remove embedded credentials, disclose or disable remote geocoding and location caching, and retain only helpers required for the intended run mode. <br>
Risk: Dependencies are not pinned, which can make installation and runtime behavior less reproducible. <br>
Mitigation: Pin and review dependencies in the deployment environment before commercial use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-hyperspectral-vegetation-stress) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF rasters, GeoJSON vectors, JSON reports, JSON run manifests, and command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include stress_level.tif, stress_index.tif, anomaly.geojson, stress_report.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
