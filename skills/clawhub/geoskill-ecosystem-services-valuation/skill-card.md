## Description: <br>
Estimates provisioning, regulating, supporting, and cultural ecosystem service values with an equivalent-factor method, producing GeoTIFF value rasters and summary JSON for local or synthetic NDVI inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and ecological planning teams use this skill to estimate ecosystem service values for ecological asset accounting, GEP estimation, occupation-compensation balance, and ecological compensation analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes bundled network, credential, and cache functionality beyond the documented offline valuation command. <br>
Mitigation: Review the bundled modules before installation, remove unused network and credential code where possible, and run the skill in a restricted environment when offline execution is expected. <br>
Risk: Hardcoded Earthdata fallback credentials are present in bundled credential code. <br>
Mitigation: Do not reuse bundled credentials; rotate any exposed credentials, clear default credential values before deployment, and provide secrets only through reviewed environment or secret-store mechanisms. <br>
Risk: The valuation method uses simplified NDVI thresholds and equivalent factors, which may produce misleading estimates for unsuitable regions, dates, or land-cover conditions. <br>
Mitigation: Validate inputs, assumptions, and outputs with local land-cover data, domain review, and sensitivity checks before using results for policy or financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-ecosystem-services-valuation) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, GeoTIFF, JSON, Text] <br>
**Output Format:** [GeoTIFF rasters, JSON summaries, output manifest, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes four service-value rasters, service totals, LULC pixel counts, and run manifest files to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and executable VERSION; artifact CHANGELOG.md and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
