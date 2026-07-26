## Description: <br>
Calculate Urban Heat Island (UHI) intensity from MODIS LST GeoTIFF data, classify heat island levels, perform temporal analysis, and output UHI maps with statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, analysts, and geospatial teams use this skill to calculate, classify, and summarize urban heat island intensity from MODIS land surface temperature rasters. It supports local single-image analysis, classification of existing UHI rasters, seasonal summaries across multiple images, and an optional place-based workflow for fetching MODIS data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional from-place workflow can send place and date requests to third-party services and run a neighboring downloader tool. <br>
Mitigation: Avoid or restrict from-place in offline-only or tightly controlled environments; use analyze, classify, and temporal with pre-downloaded local GeoTIFF inputs instead. <br>
Risk: The place-based workflow writes downloaded cache files to disk. <br>
Mitigation: Run it in a controlled workspace, review cache locations, and delete cached data when it is no longer needed. <br>
Risk: UHI results depend on input raster quality, CRS alignment, nodata handling, and the rural-reference method. <br>
Mitigation: Validate input CRS and quality bands, use a suitable rural mask or fraction, and compare outputs against known local conditions or station data before operational use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/urban-heat-analysis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash commands; CLI workflows produce GeoTIFF, JSON, and CSV outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include UHI intensity GeoTIFFs, classified GeoTIFFs, statistics sidecars, temporal summaries, and optional QA sidecars.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
