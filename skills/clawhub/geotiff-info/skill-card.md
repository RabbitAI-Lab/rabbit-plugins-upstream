## Description: <br>
Zero-dependency Python tool for reading GeoTIFF file metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
Developers, geospatial analysts, and external users use this skill to inspect GeoTIFF metadata from local files or directories without installing GIS software or third-party Python packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes bundled geospatial helper code outside the advertised local GeoTIFF metadata workflow, including network geocoding, downloads, and cache-writing behavior. <br>
Mitigation: Use the documented geotiff-info.py path for local metadata inspection, and avoid invoking _place.py or _geoskill_core helpers unless outbound geocoding, downloads, and local cache writes are intended. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geotiff-info) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, files] <br>
**Output Format:** [Human-readable text tables, JSON metadata, and optional JSON QA sidecar files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-file inspection and batch directory scanning.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and script __version__) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
