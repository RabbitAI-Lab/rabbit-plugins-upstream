## Description: <br>
Estimates forest above-ground biomass (AGB, t/ha) from SAR backscatter using linear or saturation empirical models, with C/L band support and optional ground-sample calibration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to estimate forest above-ground biomass from local SAR backscatter imagery or synthetic test scenes for forest carbon monitoring, biomass mapping, and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, downloader, cache, and credential-handling modules beyond the local biomass entrypoint. <br>
Mitigation: Review the package before installation and remove or clearly document unused helper modules before deployment. <br>
Risk: Embedded Earthdata credentials are reported in the security evidence. <br>
Mitigation: Delete embedded credentials, rotate any exposed credentials, and rely on runtime secret injection or documented environment variables. <br>
Risk: Dependencies are not pinned in requirements.txt. <br>
Mitigation: Pin dependency versions and install in an isolated environment before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-forest-biomass) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands] <br>
**Output Format:** [GeoTIFF and JSON files with optional console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces forest_biomass.tif, biomass_report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and entrypoint VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
