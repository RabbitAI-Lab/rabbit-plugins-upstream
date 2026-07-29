## Description: <br>
Downloads ISRIC SoilGrids soil property data such as pH, organic carbon, texture fractions, bulk density, and cation exchange capacity for point or bounding-box center queries across six standard depth layers at 250 m resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to query ISRIC SoilGrids soil-property predictions for specific coordinates or bounding-box center points and save the results for tabular analysis, GIS workflows, or downstream automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was flagged as suspicious because it includes under-disclosed credential-handling helpers unrelated to normal SoilGrids downloads. <br>
Mitigation: Review or remove the bundled credential module before installation unless those helpers are explicitly trusted and needed. <br>
Risk: Place-name resolution can send place names to third-party geocoding services. <br>
Mitigation: Use explicit latitude/longitude or bounding-box inputs when place names should not be sent to geocoding providers. <br>
Risk: Dependency versions are not fully pinned. <br>
Mitigation: Install with pinned, reviewed dependency versions in controlled environments. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/soilgrids-download) <br>
- [ISRIC SoilGrids API](https://rest.isric.org/soilgrids/v2.0/) <br>
- [ISRIC SoilGrids FAQ](https://www.isric.org/explore/soilgrids/faq-soilgrids) <br>
- [SoilGrids 2.0 paper](https://doi.org/10.5194/soil-7-217-2021) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, CSV, JSON, Guidance] <br>
**Output Format:** [CSV or JSON files with soil property records, optional QA JSON summaries, and console status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Records include location, property, depth, prediction values, and units; unavailable layers may be represented as NaN.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
