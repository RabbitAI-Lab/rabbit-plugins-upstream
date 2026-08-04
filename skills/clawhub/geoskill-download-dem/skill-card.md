## Description: <br>
Select, discover, download, resume, tile, mosaic, crop, and validate DEM data from Microsoft Planetary Computer, AWS Open Data, OpenTopography, USGS 3DEP, and NASA Earthdata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and other external users use this skill to plan, download, resume, mosaic, tile, crop, and validate digital elevation model data for a specified bbox, vector AOI, or supported Chinese administrative boundary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports under-disclosed credential handling, including real-looking embedded Earthdata credentials and reads from local secret files or .netrc. <br>
Mitigation: Review before installation, remove or rotate embedded credentials, avoid shared fallback credentials, and require explicit user-provided tokens for protected providers. <br>
Risk: The security evidence recommends dependency review because dependencies are not pinned to reviewed versions. <br>
Mitigation: Pin dependencies to reviewed versions before operational use and re-scan the resulting package. <br>
Risk: The skill uses external geocoding and DEM provider services, so requests may disclose AOI, administrative-place, and download intent metadata to those services. <br>
Mitigation: Confirm the relevant provider terms and privacy expectations for the intended workflow, and clarify or remove bundled geocoding or cache helpers that are not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-download-dem) <br>
- [Provider and Dataset Reference](references/sources.md) <br>
- [DEM Source And Output Selection](references/source-selection.md) <br>
- [Large-Area And Resumable Workflow](references/large-area-workflow.md) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Open Data Copernicus DEM](https://registry.opendata.aws/copernicus-dem/) <br>
- [OpenTopography API documentation](https://portal.opentopography.org/apidocs/) <br>
- [USGS National Map download tools](https://www.usgs.gov/tools/download-data-maps-national-map) <br>
- [NASA Earthdata ASTER GDEM V3 DOI](https://doi.org/10.5067/ASTER/ASTGTM.003) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON provenance or validation summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may produce local GeoTIFF files, tile directories, manifests, and provenance sidecars through its download script.] <br>

## Skill Version(s): <br>
6.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
