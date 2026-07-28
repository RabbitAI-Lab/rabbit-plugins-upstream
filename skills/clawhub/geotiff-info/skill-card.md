## Description: <br>
Zero-dependency Python CLI for reading GeoTIFF metadata from local files and directories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to inspect GeoTIFF metadata, including CRS, resolution, bands, NoData values, dimensions, corner coordinates, and batch scan output without opening GIS software. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence flags bundled credential, network geocoding, caching, and download helpers that go beyond the advertised local GeoTIFF metadata viewer. <br>
Mitigation: Review before installing, use only in trusted environments, and audit or remove the extra helper modules if local metadata inspection is the only required function. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geotiff-info) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands] <br>
**Output Format:** [Plain text tables or JSON metadata from a Python CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-file inspection and directory batch scans.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
