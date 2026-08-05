## Description: <br>
Estimate building footprint density and floor area ratio (FAR) from building footprints and heights using kernel density estimation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and urban planning teams use this skill to create building density and FAR layers from local building footprint and height rasters, or to test the workflow with synthetic offline data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network, credential, and cache code outside the main local density workflow. <br>
Mitigation: Review or remove the unrelated vendored core modules before installation, especially credentials.py, safe_download.py, _place.py, and _geoskill_core/aoi.py. <br>
Risk: Credential helper code may interact with local credential stores on machines that contain sensitive entries. <br>
Mitigation: Avoid installing on systems with sensitive ~/.netrc or ~/.geoskill/secrets.json entries unless the credential helpers are removed or isolated, and rotate any real credential represented by the hardcoded fallback. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-building-density-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Configuration] <br>
**Output Format:** [GeoTIFF raster plus JSON statistics and run manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces building_density.tif with density and FAR bands, density_stats.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
