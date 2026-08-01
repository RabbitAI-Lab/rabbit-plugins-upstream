## Description: <br>
Download JRC Global Surface Water data layers including occurrence, change, seasonality, recurrence, transition, and extent, clipped to a user-supplied bounding box as GeoTIFF files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and GIS practitioners use this skill to download JRC Global Surface Water raster layers for a selected area of interest and prepare them for local analysis or GIS workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Large GeoTIFF tile downloads can consume substantial local disk space. <br>
Mitigation: Estimate the number of intersecting tiles before large-area runs, start with a small bounding box, and download one layer at a time when storage is limited. <br>
Risk: The skill performs external network downloads and may use external geocoding when place-based lookup is used. <br>
Mitigation: Run in a virtual environment, review requirements.txt before installation, keep requests and tqdm patched, and avoid --place when external place-query disclosure is not acceptable. <br>


## Reference(s): <br>
- [JRC Global Surface Water Explorer](https://global-surface-water.appspot.com/) <br>
- [Google Earth Engine Dataset: JRC/GSW1_4/GlobalSurfaceWater](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater) <br>
- [High-resolution mapping of global surface water and its long-term changes](https://doi.org/10.1038/nature20584) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash and Python examples; the CLI writes GeoTIFF files and can write a JSON QA summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the selected layer, bounding box, tile availability, and available local disk space.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
