## Description: <br>
Calculate spectral indices from GeoTIFF imagery using pure Python, including NDVI, NDBI, NDWI, EVI, SAVI, MNDWI, AWEI, NBR, BSI, and UI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, geospatial analysts, and agent users can use this skill to calculate common remote-sensing spectral indices from GeoTIFF imagery, either one index at a time, in batch mode, or with custom formulas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security scan reports under-disclosed network and credential helper code bundled with the advertised local calculator, including hardcoded Earthdata credentials. <br>
Mitigation: Review the skill before installing, remove or rotate exposed credentials, and require credentials to be supplied through user-controlled environment variables, netrc, or local secret files. <br>
Risk: Bundled helper code may use network services, cache location lookups in the user's home directory, and read or supply credentials even though the core calculator appears local. <br>
Mitigation: Run the calculator in a restricted environment when possible, limit network and home-directory access, and remove unused geospatial helper modules from deployments that only need local GeoTIFF index calculation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/rs-index-calc) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, files, text] <br>
**Output Format:** [Markdown guidance with shell command examples; command execution can produce GeoTIFF files and stdout statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-index, batch, custom-formula, and manual band-selection workflows.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
