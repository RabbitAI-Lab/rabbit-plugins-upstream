## Description: <br>
LiDAR micro-topography, multispectral anomaly and SAR fusion for suspected archaeological site detection with anomaly grading <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and geospatial or archaeology analysts use this skill to screen DEM, Red, NIR, and SAR raster inputs or synthetic scenes for suspected archaeological site anomalies. It produces local anomaly layers, suspected-site points, reports, and a run manifest for expert review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that the package includes bundled geocoding, download, and credential-handling helpers that are not disclosed by the skill instructions. <br>
Mitigation: Treat installation as review-required; prefer a cleaned release that removes unused credential helpers, removes hardcoded credential defaults, documents network behavior, and pins dependencies. <br>
Risk: Remote-sensing anomaly detections can create false positives and should not be treated as confirmed archaeological sites. <br>
Mitigation: Use outputs as leads for expert review, compare against source rasters and contextual data, and validate findings before operational or public use. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-archaeology-site-detection) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Guidance] <br>
**Output Format:** [GeoTIFF, GeoJSON, JSON, and run manifest files with concise command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written locally and include anomaly scores, anomaly levels, suspected-site features, summary statistics, and a manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
