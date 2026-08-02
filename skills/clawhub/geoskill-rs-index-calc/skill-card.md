## Description: <br>
Calculate spectral indices from GeoTIFF imagery using pure Python without external dependencies, supporting batch, custom formulas, and automatic band detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to calculate common spectral indices from GeoTIFF imagery, including NDVI, NDBI, NDWI, EVI, SAVI, MNDWI, AWEI, NBR, BSI, and UI. It helps agents provide commands and usage guidance for single-index, batch, custom-formula, and manual band-order workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill works with local GeoTIFF paths and output destinations supplied by the user. <br>
Mitigation: Review the selected input and output paths before running generated commands, and avoid directing outputs to sensitive or shared locations unless intended. <br>
Risk: The reviewed artifact references a calculator script that is not included in the artifact. <br>
Mitigation: Review the remote repository before relying on README installation commands or executing the referenced calculator. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-rs-index-calc) <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and parameter descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced calculator writes single-band GeoTIFF result files and prints min, max, mean, standard deviation, and pixel count statistics to stdout.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
