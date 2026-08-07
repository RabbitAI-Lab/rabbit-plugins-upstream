## Description: <br>
Sentinel-1 GRD preprocessing pipeline for dB conversion, pixel-aligned bbox clipping, dual-polarization QA, and local GeoTIFF and JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run a local Sentinel-1 GRD preprocessing workflow over a WGS84 bounding box or local raster input. It is suited for generating clipped sigma0 dB GeoTIFF outputs, processing logs, and run manifests for downstream remote-sensing analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the package ships undisclosed credential, geocoding, download, and cache code, including a real-looking embedded password. <br>
Mitigation: Review before installing, remove embedded credential defaults, rotate any exposed credentials, and require explicit user-provided environment variables or secret files. <br>
Risk: The advertised CLI is local raster processing, but bundled helpers include network geocoding/download behavior and home-directory caches that may surprise users. <br>
Mitigation: Run in a network-restricted sandbox unless those helpers are reviewed, documented, and intentionally enabled for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sentinel1-tile-management) <br>
- [README](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [CHANGELOG](artifact/CHANGELOG.md) <br>
- [Semantic Versioning](https://semver.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; runtime outputs are GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces sigma0_db.tif, processing_log.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; artifact changelog/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
