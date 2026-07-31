## Description: <br>
Automatic water body extraction from multi-band satellite imagery using NDWI and MNDWI indices, with support for Landsat 8/9 and Sentinel-2 inputs, threshold optimization, and vector output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to extract water masks, boundaries, and statistics from Landsat 8/9 or Sentinel-2 GeoTIFF imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill claims local-only behavior, but security evidence identifies networked place lookup and download behavior. <br>
Mitigation: Use local --input workflows or --no-auto-fetch when offline or privacy-sensitive operation is required, and avoid --place unless external network access is approved. <br>
Risk: Security evidence identifies embedded fallback Earthdata credentials. <br>
Mitigation: Remove or rotate embedded credentials before use and provide approved credentials through managed environment variables or a secrets manager. <br>
Risk: The security verdict is suspicious for restricted or privacy-sensitive environments. <br>
Mitigation: Review and scan the skill before deployment, document any permitted external services, and restrict execution to environments where network downloads are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/water-body-extraction) <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated outputs may include GeoTIFF raster masks, GeoJSON or Shapefile vectors, QA JSON, and text or JSON statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-image extraction, batch processing, threshold calculation, optional vector export, and optional JSON statistics.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
