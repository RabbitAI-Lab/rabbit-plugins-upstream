## Description: <br>
Estimate impervious surface fraction from multi-band Sentinel-2 satellite imagery using NDBI, NDVI, and MNDWI, with support for binary classification, continuous fraction estimation, zone aggregation, and change detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to map urban impervious surfaces from Sentinel-2 imagery, compute impervious ratios for zones such as watersheds or administrative units, and compare built-up surface change across years. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The remote-download path can fall back to synthetic demo data when downloaded imagery is not suitable for the five-band analysis, which can make results misleading if treated as real-world output. <br>
Mitigation: Review console output and the output manifest before relying on results; confirm whether the run used real imagery, verify downloaded paths and data-source metadata, or provide a validated five-band raster directly. <br>
Risk: The CLI reads local geospatial inputs, writes analysis artifacts under the selected output directory, and may contact Microsoft Planetary Computer when bounding-box or date-range inputs are used. <br>
Mitigation: Run it in a controlled workspace, choose output paths deliberately, inspect generated files, and pin dependencies in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-impervious-surface-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated outputs include GeoTIFF, CSV, JSON, and console text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces impervious fraction and binary rasters, optional zone summaries, optional change rasters, optional accuracy metrics, and an output manifest.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
