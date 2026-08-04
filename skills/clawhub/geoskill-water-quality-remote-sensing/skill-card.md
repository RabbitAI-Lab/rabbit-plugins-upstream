## Description: <br>
Estimate water quality parameters from multispectral satellite imagery using red and green bands, with optional NIR and SWIR inputs for additional indices and report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to compute water-quality indices from multispectral raster bands, compare remote-sensing inputs, and generate machine-readable and human-readable assessment outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unpinned Python dependencies may change behavior or introduce supply-chain exposure between installs. <br>
Mitigation: Review the dependency set before installation and pin vetted versions in the target environment. <br>
Risk: Advertised AOI or bounding-box download workflows may send geographic area and date-range information to Microsoft Planetary Computer and cache data locally. <br>
Mitigation: Use approved areas and date ranges, review cache location and retention, and avoid sensitive AOI values unless the data-sharing path is acceptable. <br>
Risk: The documentation advertises bbox/date-range download usage, while the bundled script accepts local red and green raster paths. <br>
Mitigation: Verify the installed release behavior before relying on automated download workflows in production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-quality-remote-sensing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated run artifacts include JSON, HTML, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces water-quality index summaries and local report files when run against suitable raster inputs.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
