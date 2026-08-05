## Description: <br>
Estimates GPP and NPP with a simplified CASA/VPM light-use-efficiency model, using PAR, FPAR, temperature stress, and water stress to produce carbon flux rasters, daily time series, and a carbon budget. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental researchers use this skill to run local ecosystem carbon-flux estimates for a bounding box or local raster input. It supports regional productivity mapping, carbon budget assessment, ecosystem model forcing, and carbon source/sink analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented CLI is an offline local carbon-flux calculator, but the package includes under-disclosed helper code for credentials, downloads, and geocoding, including a hardcoded Earthdata credential. <br>
Mitigation: Review or remove the helper modules before installation, rotate the embedded credential, and avoid installing in environments with sensitive ~/.netrc, ~/.geoskill/secrets.json, or environment credentials until the publisher resolves the issue. <br>
Risk: Optional helper behavior may use third-party location lookup or download paths that are outside the documented offline workflow. <br>
Mitigation: Prefer synthetic or local raster input modes for isolated runs, and audit any geocoding or download behavior before enabling network access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-carbon-flux-estimation) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [GeoTIFF raster files, JSON reports, and Markdown or shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary files include carbon_flux.tif, flux_timeseries.json, carbon_budget.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
