## Description: <br>
Spatial scan statistics, kernel density, environment association and accessibility for public health spatial analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Public health analysts, geospatial developers, and external users use this skill to run local spatial analysis for disease hot spots, environmental association, and healthcare accessibility from synthetic data or local multi-band GeoTIFF inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, credential, and caching helpers that are not fully reflected in the offline-first documentation. <br>
Mitigation: Review helper modules before deployment, run with synthetic or local inputs when possible, and document or disable network paths that are not required for the intended workflow. <br>
Risk: A hardcoded Earthdata password fallback is present in the packaged credential helper. <br>
Mitigation: Remove the fallback credential, rotate any exposed credential if applicable, and require user-managed credentials through environment variables, netrc, or a secrets file. <br>
Risk: Local cache files may retain geocoding or workflow state. <br>
Mitigation: Document cache locations and clear local caches when working with sensitive project locations or regulated public-health data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-public-health-spatial) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, JSON, GeoTIFF] <br>
**Output Format:** [CLI guidance plus generated GeoTIFF, JSON report, and run manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include case_density.tif, scan_result.json, accessibility.tif, health_report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
