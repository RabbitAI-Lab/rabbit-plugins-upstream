## Description: <br>
Calculates Urban Heat Island (UHI) intensity from MODIS Land Surface Temperature GeoTIFF data, classifies heat island levels, performs temporal analysis, and outputs UHI maps with statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and urban climate teams use this skill to compute UHI intensity, classify heat island severity, and generate GeoTIFF, JSON, or CSV outputs from local MODIS LST rasters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional from-place workflow is experimental, underdocumented, and may invoke external geocoding or data-download services. <br>
Mitigation: Prefer analyze, classify, and temporal workflows on local GeoTIFF inputs for routine use; review from-place behavior and external services before enabling it. <br>
Risk: Results can be misleading when input rasters have mismatched CRS, cloud contamination, nodata issues, or an unsuitable rural reference. <br>
Mitigation: Align raster CRS and extent, apply QC or cloud masks, inspect nodata handling, and validate outputs against local temperature observations or domain expectations. <br>
Risk: Unpinned geospatial dependencies can affect reproducibility, especially where rasterio and GDAL versions differ. <br>
Mitigation: Pin numpy, rasterio, and GDAL-compatible environment versions for production or repeatable analyses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/urban-heat-analysis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [Imhoff et al. 2010 UHI remote sensing paper](https://doi.org/10.1016/j.rse.2009.10.008) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated analysis files include GeoTIFF plus JSON or CSV statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local GeoTIFF inputs; outputs depend on raster CRS alignment, nodata handling, rural reference selection, and optional command flags.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
