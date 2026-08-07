## Description: <br>
Calculates Urban Heat Island intensity from MODIS Land Surface Temperature GeoTIFF data, classifies heat levels, performs temporal analysis, and writes maps with statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and environmental teams use this skill to compute and classify urban heat island intensity from local MODIS LST raster inputs and compare heat patterns over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security evidence reports a bundled hardcoded Earthdata credential fallback. <br>
Mitigation: Remove or rotate fallback credentials before shared deployment and rely on environment variables, netrc, or user-managed secrets instead. <br>
Risk: Optional place resolution and from-place workflows can send place names, coordinates, dates, or download requests to external geocoding and data services. <br>
Mitigation: Disclose network use before execution, prefer local GeoTIFF inputs in sensitive contexts, and disable optional online resolvers where privacy requirements demand it. <br>
Risk: The server security verdict is suspicious because network geocoding/download behavior is under-disclosed relative to the mostly local raster-analysis workflow. <br>
Mitigation: Review the package before installing in shared or sensitive environments and document when optional downloader or geocoding paths are used. <br>


## Reference(s): <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [Remote sensing of the urban heat island effect across biomes in the continental USA](https://doi.org/10.1016/j.rse.2009.10.008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI examples; generated agent commands may produce GeoTIFF, JSON, and CSV files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include UHI intensity rasters, classified rasters, statistics sidecars, and temporal summaries.] <br>

## Skill Version(s): <br>
5.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
