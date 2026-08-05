## Description: <br>
Performs pixel-by-pixel cross-tabulation of two land cover classification rasters to produce a transition matrix, change area statistics, and Sankey flow data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and GIS practitioners use this skill to quantify land cover transitions between two classification rasters, including cropland loss, built-up expansion, and land-change ledger workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports under-disclosed network, caching, and credential-handling support code, including hardcoded Earthdata credentials. <br>
Mitigation: Review or remove the bundled credential, download, AOI, and geocoding helpers before installation; rotate or remove embedded Earthdata credentials and document any network or credential behavior. <br>
Risk: The public description emphasizes local raster processing while packaged support code has broader behavior. <br>
Mitigation: Limit deployment to the documented local raster workflow unless the broader support modules have been reviewed and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lulc-change-matrix) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples; generated agent workflows may produce CSV, JSON, GeoTIFF, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces transition_matrix.csv, change_areas.json, sankey.json, change_map.tif, and output-manifest.json when the bundled CLI is executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
