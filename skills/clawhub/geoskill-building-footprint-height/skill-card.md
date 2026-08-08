## Description: <br>
Extract building footprints and estimate height, floor count proxy, and volume from DSM/DTM/LiDAR data for 2.5D urban modeling, population downscaling, and risk exposure analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and urban risk teams use this skill to estimate building heights, floor proxies, volumes, and quality flags from elevation data and building footprints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional bbox or AOI workflow downloads elevation data from Microsoft Planetary Computer. <br>
Mitigation: Use the download path only where outbound access and AOI disclosure to that service are approved. <br>
Risk: Production use depends on geospatial libraries and external input data quality. <br>
Mitigation: Pin and review dependencies, especially fiona, numpy, rasterio, shapely, and geoskill-data-fetcher, and validate DSM/DTM, LiDAR, and footprint inputs before relying on results. <br>
Risk: Estimated floors and heights can be misleading when source data are coarse, incomplete, or affected by trees and mixed pixels. <br>
Mitigation: Review the generated quality codes, quality flags, and QA output before using estimates for planning, exposure, or downstream modeling. <br>


## Reference(s): <br>
- [Building height standards](references/building_height_standards.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-building-footprint-height) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands, Configuration] <br>
**Output Format:** [GeoJSON, CSV, JSON, HTML, and NumPy raster files, with Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes building height outputs, quality flags, request metadata, dataset and output manifests, and QA results to a local output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
