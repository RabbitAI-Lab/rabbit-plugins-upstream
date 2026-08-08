## Description: <br>
Sample elevation or imagery values along a path and produce profile charts and CSV. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and external users can use this skill to resample local or synthetic DEM data along a path and generate elevation profile charts plus CSV/JSON sample tables for terrain analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package bundles credential-management code with a hardcoded Earthdata password. <br>
Mitigation: Remove or isolate the credential module and delete and rotate the embedded password before installation in environments with real credentials. <br>
Risk: The package includes under-disclosed network lookup and download helpers even though the documented chart workflow is local. <br>
Mitigation: Review, disclose, or remove the geocoding and download helpers, and restrict execution to the expected local chart workflow when network access is not needed. <br>
Risk: The package may be installed in environments containing sensitive geospatial data. <br>
Mitigation: Review the package before use with sensitive data and run the documented offline or synthetic mode where possible. <br>
Risk: Vendored provenance metadata is inconsistent with the chart generator release. <br>
Mitigation: Fix the vendored provenance metadata before release review or downstream redistribution. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-profile-chart-generator) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, guidance] <br>
**Output Format:** [PNG, CSV, JSON, GeoTIFF, run manifest JSON, and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates profile.png, profile.csv, profile.json, profile_dem.tif, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION; artifact CHANGELOG/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
