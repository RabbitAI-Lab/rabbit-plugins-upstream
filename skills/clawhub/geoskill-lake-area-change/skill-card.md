## Description: <br>
Extracts multi-temporal NDWI/MNDWI water bodies, reconstructs lake-area time series, and analyzes change trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial teams use this skill to run local lake-water extraction from multi-band GeoTIFF inputs or synthetic test data, then produce lake boundary and area-trend artifacts for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed credential, geocoding, downloader, and persistent-cache helper code outside the published lake-analysis workflow. <br>
Mitigation: Review or remove those bundled helpers before deployment, replace the hardcoded Earthdata fallback, and document any geocoding or network use. <br>
Risk: Unpinned geospatial dependencies may change behavior across environments. <br>
Mitigation: Pin and scan dependencies before installation, then run the included synthetic and local-raster tests in the target environment. <br>
Risk: Location queries and local credential files can be sensitive if this package is used beyond the documented synthetic or local-raster workflow. <br>
Mitigation: Treat AOI inputs and user credential files as sensitive, avoid logging secrets, and prefer environment- or secret-manager-supplied credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lake-area-change) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated local files including GeoTIFF, GeoJSON, JSON, and an output manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes water_index.tif, lake_boundaries.geojson, area_timeseries.json, and output-manifest.json when the CLI is executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
