## Description: <br>
利用 NDSI 指数与温度阈值提取积雪/冰体覆盖范围，输出积雪栅格与面积统计 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local snow and ice remote-sensing workflows over a WGS84 bounding box or local raster input. It supports NDSI-based snow/ice extraction with optional temperature filtering and produces raster output plus area statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper code includes credential, geocoding, download, and cache behavior that is broader than the documented offline snow/ice mapping workflow. <br>
Mitigation: Review the package before installation in environments with API keys, .netrc files, or sensitive location queries, and prefer synthetic or local-input mode unless the extra helper behavior is documented and needed. <br>
Risk: The documented purpose emphasizes offline local processing, while the security evidence notes under-disclosed network and home-directory cache helpers. <br>
Mitigation: Run in a constrained environment, inspect configuration and environment variables before use, and require explicit documentation before enabling any network-backed workflows. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance and CLI output files, including GeoTIFF and JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs include result.tif, output-manifest.json, and snow area statistics; synthetic mode can run without network access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
