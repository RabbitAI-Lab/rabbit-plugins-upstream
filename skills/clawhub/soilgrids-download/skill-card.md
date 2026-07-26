## Description: <br>
Download ISRIC SoilGrids soil property data, including pH, organic carbon, sand/silt/clay fractions, bulk density, and cation exchange capacity, with point and bbox center-point queries across six standard depth layers at 250m resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial workflows use this skill to query ISRIC SoilGrids soil-property estimates for a point, bbox center point, or resolved place name and save the results for analysis or GIS integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name queries may be sent to third-party geocoding services. <br>
Mitigation: Use explicit --lat/--lon or --bbox for sensitive locations, and treat place names as data that may leave the local environment. <br>
Risk: Dependencies use broad minimum-version constraints. <br>
Mitigation: Pin reviewed dependency versions before use in production or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/soilgrids-download) <br>
- [ISRIC SoilGrids API](https://rest.isric.org/soilgrids/v2.0/) <br>
- [ISRIC SoilGrids FAQ](https://www.isric.org/explore/soilgrids/faq-soilgrids) <br>
- [SoilGrids 2.0 citation](https://doi.org/10.5194/soil-7-217-2021) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated data files are CSV, JSON, and optional QA JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries SoilGrids over HTTP and can optionally resolve place names through third-party geocoding before writing local output files.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
