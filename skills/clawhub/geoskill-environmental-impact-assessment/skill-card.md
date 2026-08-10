## Description: <br>
Combines normalized, weighted environmental pressure factors with cumulative-effect modeling to produce impact-index and impact-grade GeoTIFF outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental assessment teams use this skill for construction-project, planning-level, and cumulative environmental impact screening from a bounding-box synthetic scenario or a local multi-band pressure raster. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence flags under-disclosed network, caching, and credential-handling code, including embedded Earthdata fallback credentials. <br>
Mitigation: Review the package in isolation before installation, remove embedded credentials, and avoid providing secrets until credential scope and network/cache behavior are disclosed or disabled. <br>
Risk: The skill can generate environmental impact scores from synthetic or user-provided pressure factors, which may be mistaken for authoritative regulatory findings. <br>
Mitigation: Require qualified environmental review, document input sources and weights, and validate outputs against accepted EIA methods before using results for decisions. <br>
Risk: Optional geocoding, download, and cache helpers in the artifact may persist place queries or fetch remote data outside the main offline workflow. <br>
Mitigation: Run with explicit local inputs where possible, use a controlled workspace, disable or clear caches, and restrict outbound network access for sensitive assessments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-environmental-impact-assessment) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands] <br>
**Output Format:** [GeoTIFF raster files, JSON parameter and manifest files, and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces impact_index.tif, impact_grade.tif, eia_params.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and CLI VERSION constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
