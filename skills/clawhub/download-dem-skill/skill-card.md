## Description: <br>
Select, discover, download, resume, tile, mosaic, crop, and validate DEM data from public and optional-key elevation providers, including Chinese administrative-area lookup through map.ruiduobao.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial data users use this skill to plan, download, validate, and document DEM outputs for city-to-country areas of interest from multiple elevation data sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts DEM and administrative-boundary providers during normal operation. <br>
Mitigation: Run it only where outbound network access to the selected providers is acceptable, and review the planned source before download. <br>
Risk: DEM downloads can write large files or directories near the selected output path. <br>
Mitigation: Plan first, inspect estimated area, asset count, and output mode, and choose an output location with adequate storage. <br>
Risk: OpenTopography and Earthdata credentials are optional but may be used when configured. <br>
Mitigation: Set provider credentials only when those sources are intended, and avoid sharing logs or files that could expose credential-bearing requests. <br>
Risk: Downloaded elevation datasets may have provider-specific licenses, attribution requirements, surface classes, and vertical datums. <br>
Mitigation: Review provider terms and metadata before redistributing outputs or using them for sensitive geospatial analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/download-dem-skill) <br>
- [Provider and Dataset Reference](artifact/references/sources.md) <br>
- [DEM Source And Output Selection](artifact/references/source-selection.md) <br>
- [Large-Area And Resumable Workflow](artifact/references/large-area-workflow.md) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Open Data Copernicus DEM](https://registry.opendata.aws/copernicus-dem/) <br>
- [OpenTopography Global DEM API](https://portal.opentopography.org/API/globaldem) <br>
- [USGS The National Map Access API](https://tnmaccess.nationalmap.gov/api/v1/docs) <br>
- [NASA Earthdata ASTER GDEM V3](https://doi.org/10.5067/ASTER/ASTGTM.003) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated DEM artifacts include GeoTIFF files, tile directories, JSON plans, manifests, validation reports, and provenance reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May contact DEM and administrative-boundary providers and may write large files near the user-selected output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
