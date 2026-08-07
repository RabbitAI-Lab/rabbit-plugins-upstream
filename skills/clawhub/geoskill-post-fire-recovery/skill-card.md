## Description: <br>
Classifies post-fire burn severity with dNBR and estimates vegetation recovery trajectory, slope, and recovery time from NDVI time series. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and disaster-recovery teams use this skill to analyze user-provided or synthetic raster scenes for burn severity and vegetation recovery planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the package contains under-disclosed network, credential, and home-directory cache code. <br>
Mitigation: Review the bundled helper modules before installation and install only where unexpected network-capable helpers and local credential reads are acceptable. <br>
Risk: The security evidence says exposed Earthdata fallback credentials are present. <br>
Mitigation: Revoke or remove exposed fallback credentials before deployment. <br>
Risk: The security evidence verdict is suspicious. <br>
Mitigation: Put this skill in Review before installation and document or remove the bundled geocoding, downloader, cache, and credential helper behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-post-fire-recovery) <br>
- [README](artifact/README.md) <br>
- [Skill source instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, GeoTIFF] <br>
**Output Format:** [GeoTIFF rasters and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces burn severity, dNBR, recovery slope, recovery year, recovery trajectory, and output manifest files in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
