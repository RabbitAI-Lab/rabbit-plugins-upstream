## Description: <br>
Selects, discovers, downloads, resumes, tiles, mosaics, crops, and validates DEM data from Microsoft Planetary Computer, AWS Open Data, OpenTopography, USGS 3DEP, and NASA Earthdata for city-to-country AOIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and mapping operators use this skill to plan and run DEM downloads for an area of interest, select an appropriate provider and dataset, produce GeoTIFF mosaics or resumable tile directories, and report provenance and validation status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact external DEM providers and use optional provider credentials such as OPENTOPOGRAPHY_API_KEY or EARTHDATA_TOKEN. <br>
Mitigation: Use credentials only for the selected provider, avoid logging or persisting tokens or signed URLs, and review provider terms before redistributing downloaded data. <br>
Risk: DEM downloads can write large output, manifest, partial-download, and cache files under the selected output location. <br>
Mitigation: Run planning first, inspect area, pixel, and asset estimates, choose tile mode for large AOIs, and confirm storage capacity before starting transfers. <br>
Risk: DEM sources differ in surface model class, vertical datum, coverage, licensing, and attribution requirements. <br>
Mitigation: Report the selected source, DSM/DTM class, vertical datum, validation status, official source URLs, and any fallback, resampling, or raw-tile overcoverage. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/download-dem-skil) <br>
- [DEM source and output selection](references/source-selection.md) <br>
- [Large-area and resumable workflow](references/large-area-workflow.md) <br>
- [Provider and dataset reference](references/sources.md) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Open Data Copernicus DEM](https://registry.opendata.aws/copernicus-dem/) <br>
- [OpenTopography API documentation](https://portal.opentopography.org/apidocs/) <br>
- [USGS TNM Access API](https://tnmaccess.nationalmap.gov/api/v1/docs) <br>
- [NASA Earthdata ASTER GDEM V3](https://doi.org/10.5067/ASTER/ASTGTM.003) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON/provenance file descriptions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow may direct the agent to produce GeoTIFF files, tile directories, manifests, partial-download files, cache files, and validation reports through the bundled script.] <br>

## Skill Version(s): <br>
2.2.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
