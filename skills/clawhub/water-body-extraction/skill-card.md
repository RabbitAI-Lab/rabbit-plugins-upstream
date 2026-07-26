## Description: <br>
Automatic water body extraction from multi-band satellite imagery using NDWI and MNDWI indices, with support for Landsat 8/9 and Sentinel-2, Otsu threshold optimization, and vector output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing users use this skill to extract raster water masks, optional vector boundaries, and statistics from Landsat 8/9 or Sentinel-2 imagery. It can process local GeoTIFFs and also offers place-based scene lookup when enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes online place lookup and scene-fetch behavior even though some documentation describes local-only processing. <br>
Mitigation: Use local GeoTIFF inputs with --no-auto-fetch when offline-only or controlled processing is required. <br>
Risk: Place names or sensitive areas of interest may be sent to external geocoding or scene services when --place is used. <br>
Mitigation: Avoid --place for sensitive locations; provide explicit local inputs and review network behavior before deployment. <br>
Risk: Geospatial dependencies and downloaded imagery sources can affect reproducibility and production reliability. <br>
Mitigation: Pin or update dependencies deliberately, keep source imagery under review, and validate outputs against trusted reference data before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/water-body-extraction) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated geospatial files such as GeoTIFF masks, vector boundaries, JSON statistics, and QA summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on user-provided imagery or optional online scene lookup; users should review geospatial results before relying on them.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
