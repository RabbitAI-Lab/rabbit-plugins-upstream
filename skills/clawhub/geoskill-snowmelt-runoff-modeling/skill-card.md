## Description: <br>
Degree-day-factor snowmelt runoff modeling that produces a daily runoff hydrograph, snow-cover depletion curve, JSON time series, and runoff-depth raster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, hydrology analysts, and geospatial engineers use this skill to run local snowmelt runoff simulations for high-elevation or high-latitude basins, including offline synthetic validation and DEM-based workflows. It helps generate runoff time series, snow-cover curves, and raster outputs for water-resource assessment, spring melt analysis, and flood-planning support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security review flags bundled credential and network helper modules that are broader than the advertised local snowmelt workflow. <br>
Mitigation: Review the package before installing it in environments with real credentials or sensitive project locations; remove or disable credential, geocoding, and download helpers unless they are explicitly needed. <br>
Risk: A hardcoded Earthdata fallback credential path is present in bundled helper code according to the server security guidance. <br>
Mitigation: Do not rely on fallback credentials; use explicit environment-based credentials only in controlled environments, or remove the credential helper from deployments that only need the offline snowmelt command. <br>
Risk: The snowmelt model can synthesize temperature and snowpack inputs, so outputs may be unsuitable for operational decisions without local calibration and input validation. <br>
Mitigation: Validate DEM, temperature, snow water equivalent, degree-day factor, lapse rate, and melt-threshold assumptions against trusted local data before using results for planning or response decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-snowmelt-runoff-modeling) <br>
- [Skill README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with command examples; generated workflow outputs include GeoTIFF and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces runoff_depth.tif, runoff_time_series.json, and output-manifest.json when the generated commands are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
