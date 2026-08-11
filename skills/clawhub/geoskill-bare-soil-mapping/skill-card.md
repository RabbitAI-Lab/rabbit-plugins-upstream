## Description: <br>
Maps bare soil by fusing Bare Soil Index, brightness, and local texture thresholds with Otsu auto-thresholding, producing bare-soil GeoTIFF, BSI raster, area statistics, and a run manifest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and land-monitoring teams use this skill to map bare soil or bare land from synthetic scenes or user-provided multi-band surface reflectance GeoTIFFs. It supports soil erosion baselines, early desertification screening, construction-site exposed-land checks, and arid-region land-cover mapping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the documented mapper is mostly local, but the package also bundles network, downloader, and credential-handling helpers, including plaintext fallback credentials. <br>
Mitigation: Review the package before installing it in an environment with valuable credentials; remove or isolate the bundled helper modules when they are not needed, and rotate the exposed Earthdata credential if it is real. <br>
Risk: Bundled network-capable helpers can conflict with the documented offline posture of the bare-soil mapping command. <br>
Mitigation: Run the mapper in a restricted or offline environment unless network helpers are explicitly required, and use synthetic mode or local GeoTIFF inputs for offline workflows. <br>
Risk: The mapping workflow depends on correct blue, green, red, NIR, and SWIR band ordering and threshold choices; incorrect inputs can produce misleading bare-soil masks or area statistics. <br>
Mitigation: Validate input band order and geospatial metadata before use, inspect the generated manifest and area JSON, and compare automatic Otsu thresholds against known reference areas for the intended geography. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-bare-soil-mapping) <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoTIFF and JSON files, with command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bare_soil.tif, bsi.tif, bare_soil_area.json, and output-manifest.json; accepts synthetic scenes or local multi-band GeoTIFF input.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
