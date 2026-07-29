## Description: <br>
Selects, discovers, downloads, resumes, tiles, mosaics, crops, and validates DEM data from multiple public and optional credentialed providers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial agents use this skill to plan and retrieve DEM data for a WGS84 bounding box, vector AOI, or Chinese administrative place name, then return GeoTIFF mosaics or resumable tile directories with validation metadata. Review credential handling before use in sensitive environments because the security evidence flags under-disclosed credential behavior and plaintext fallback Earthdata credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/download-dem) <br>
- [Provider and Dataset Reference](references/sources.md) <br>
- [DEM Source And Output Selection](references/source-selection.md) <br>
- [Large-Area And Resumable Workflow](references/large-area-workflow.md) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Open Data Copernicus DEM Registry](https://registry.opendata.aws/copernicus-dem/) <br>
- [NASA Earthdata ASTER GDEM V3](https://doi.org/10.5067/ASTER/ASTGTM.003) <br>
- [Chinese administrative AOI service](https://map.ruiduobao.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus generated GeoTIFF, tile directories, JSON provenance, manifests, and validation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should disclose the selected provider, dataset, vertical datum, surface type, credential fallback, skipped assets, overcoverage, resampling, and validation status when available.] <br>

## Skill Version(s): <br>
2.2.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
