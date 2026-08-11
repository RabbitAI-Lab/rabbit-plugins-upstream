## Description: <br>
Performs VCA or N-FINDR endmember extraction and NNLS linear spectral unmixing for hyperspectral imagery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial engineers, and remote-sensing analysts use this skill to extract spectral endmembers, estimate per-pixel abundances, and generate residual diagnostics from synthetic or local hyperspectral GeoTIFF data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The advertised offline hyperspectral workflow includes unrelated bundled geocoding, download, and credential-handling modules. <br>
Mitigation: Review the package before installation, prefer a release that removes unused network and credential code, and run the skill in a network-restricted environment unless network behavior is documented and required. <br>
Risk: ClawHub security evidence reports hardcoded fallback credentials in bundled code. <br>
Mitigation: Use an updated package that rotates and removes embedded secrets, and scan the installed artifact before running it in an environment with sensitive local credentials. <br>
Risk: ClawHub security guidance calls for dependency pinning before use. <br>
Mitigation: Install in an isolated environment with pinned and reviewed versions of numpy, rasterio, and scipy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-hyperspectral-unmixing) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [License](artifact/LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash commands; runtime outputs include GeoTIFF, JSON, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces abundance maps, residual RMSE maps, extracted endmember spectra, and an output manifest when the CLI is executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
