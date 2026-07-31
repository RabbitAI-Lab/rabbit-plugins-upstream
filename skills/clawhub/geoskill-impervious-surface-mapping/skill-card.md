## Description: <br>
Estimate impervious surface fraction from multi-band Sentinel-2 imagery using NDBI, NDVI, and MNDWI, with binary or continuous outputs, zone aggregation, and change detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to estimate impervious surface coverage from Sentinel-2 imagery, summarize ratios by zones such as watersheds or administrative areas, and compare built-up surface changes over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may contact Microsoft Planetary Computer with bounding-box or area-of-interest and date parameters when download mode is used. <br>
Mitigation: Use local rasters in sensitive environments unless external download is intended, and review outbound network use before deployment. <br>
Risk: Geospatial outputs depend on local raster/vector input quality, band ordering, thresholds, and optional training data. <br>
Mitigation: Validate input rasters and review generated GeoTIFF, CSV, JSON, and manifest outputs before using results in operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-impervious-surface-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated GeoTIFF, CSV, JSON, and manifest files when the script is executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces impervious_fraction.tif, impervious_binary.tif, optional zones_summary.csv, optional change.tif, optional accuracy.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
