## Description: <br>
Fuses InSAR deformation rate, SAR backscatter change, and DEM-derived slope to detect suspected landslides and produce risk-ranked geospatial outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local SAR-based landslide screening on real GeoTIFF inputs or synthetic bounding-box scenarios and produce suspected landslide polygons, risk rasters, and summary data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security review reports under-documented network and credential-handling code, including embedded Earthdata credentials. <br>
Mitigation: Review before installation, run in an isolated environment, remove and rotate embedded credentials, and deny network or local credential access unless the publisher clearly documents and remediates it. <br>
Risk: Bounding-box synthetic mode and threshold-based SAR screening can produce outputs that are not suitable as final hazard determinations. <br>
Mitigation: Treat outputs as screening results and validate them with authoritative geotechnical or remote-sensing review before operational hazard decisions. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>
- [Release changelog](CHANGELOG.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-landslide-detection) <br>


## Skill Output: <br>
**Output Type(s):** [files, GeoJSON, GeoTIFF, JSON, shell commands] <br>
**Output Format:** [GeoJSON, GeoTIFF, JSON, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes landslides.geojson, deformation_rate.tif, risk_score.tif, risk_summary.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
