## Description: <br>
Automatically extract water bodies from Landsat 8/9 or Sentinel-2 satellite images using NDWI/MNDWI indices with optional Otsu thresholding and vector output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing teams use this skill to extract water masks and water-body boundaries from Landsat 8/9 or Sentinel-2 GeoTIFF imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The --place workflow may send location queries, dates, and cloud-filter parameters to external services despite local-only processing claims. <br>
Mitigation: For offline or sensitive work, use explicit local --input GeoTIFF files and avoid --place unless the publisher updates the privacy disclosure and network controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-body-extraction) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; workflows can write GeoTIFF raster masks, GeoJSON or Shapefile vectors, and JSON statistics or QA summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-image extraction, batch processing, threshold analysis, optional vector export, and optional QA JSON output.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
