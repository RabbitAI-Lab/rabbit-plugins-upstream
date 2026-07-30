## Description: <br>
Creates multi-temporal image composites from local GeoTIFF files with cloud masking and median, mean, maxNDVI, or minRed methods for Landsat and Sentinel-2 band conventions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to compose multiple Landsat or Sentinel-2 GeoTIFF scenes, apply cloud masking, and generate composite raster outputs or previews for downstream remote-sensing analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The from-place workflow can send location names to external geocoding services and invoke downloader skills. <br>
Mitigation: Review before installing or executing; use local composite mode when external lookups are not acceptable and disable Nominatim with --no-nominatim where appropriate. <br>
Risk: Bundled Earthdata fallback credentials are present. <br>
Mitigation: Remove bundled fallback credentials or override them with controlled user-provided credentials before installation or execution. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/image-composite) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts are GeoTIFF, PNG preview, and optional JSON QA files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local compositing reads and writes filesystem data; from-place workflows may perform external geocoding and invoke downloader skills.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
