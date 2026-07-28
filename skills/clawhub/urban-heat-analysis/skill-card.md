## Description: <br>
Calculate Urban Heat Island (UHI) intensity from MODIS Land Surface Temperature GeoTIFF data, classify heat island levels, perform temporal analysis, and output maps with statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, urban planners, and climate researchers use this skill to compute and classify urban heat island intensity from local MODIS LST GeoTIFFs and to summarize seasonal patterns across multiple images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential-management code includes embedded Earthdata fallback credentials and helpers that read local credential stores. <br>
Mitigation: Audit or remove the credential-management code before installation, and avoid running the skill where sensitive ~/.netrc or ~/.geoskill/secrets.json files are present. <br>
Risk: Place-based workflows may contact external geocoding or data services. <br>
Mitigation: Prefer local GeoTIFF-only analyze, classify, and temporal workflows when network calls are not acceptable, or run the skill under explicit network controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/urban-heat-analysis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [NASA Earthdata Login](https://urs.earthdata.nasa.gov/) <br>
- [Imhoff et al. 2010, Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2009.10.008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, GeoTIFF files, JSON, CSV] <br>
**Output Format:** [Markdown guidance with shell commands; generated analysis artifacts are GeoTIFF maps with JSON or CSV statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include UHI intensity rasters, classified heat island rasters, temporal summaries, statistics sidecars, and QA sidecars depending on the selected command.] <br>

## Skill Version(s): <br>
0.3.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
