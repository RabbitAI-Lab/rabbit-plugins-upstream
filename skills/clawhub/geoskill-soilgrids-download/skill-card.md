## Description: <br>
Download global soil property data from ISRIC SoilGrids for specified locations and depths at 250m resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental data users can use this skill to query SoilGrids soil properties such as pH, organic carbon, texture, bulk density, and cation exchange capacity for point locations or bbox center points. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes unrelated credential-handling utilities with a hardcoded Earthdata password and reads local credential stores. <br>
Mitigation: Review, remove, or isolate the credential utilities before use, and run the skill away from sensitive ~/.netrc or ~/.geoskill/secrets.json files unless the publisher is trusted. <br>
Risk: Using place-name lookup can send the place name to third-party geocoding services. <br>
Mitigation: Use explicit latitude/longitude or bbox coordinates for sensitive locations, and review disclosure requirements before enabling place-name queries. <br>


## Reference(s): <br>
- [ISRIC SoilGrids API](https://rest.isric.org/soilgrids/v2.0/) <br>
- [ISRIC SoilGrids FAQ](https://www.isric.org/explore/soilgrids/faq-soilgrids) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated data files are CSV or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional QA summary JSON can be written alongside query outputs.] <br>

## Skill Version(s): <br>
5.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
