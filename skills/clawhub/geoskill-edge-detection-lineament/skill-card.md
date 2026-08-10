## Description: <br>
Runs Canny or Sobel edge detection with probabilistic Hough transform to extract lineaments from raster geodata and produce edge raster and line-segment outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and geoscience workflows use this skill to run local edge detection and lineament extraction over synthetic or local raster inputs, then inspect GeoTIFF, GeoJSON, and manifest outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed geocoding, downloader, caching, and credential modules, including hardcoded credentials, even though the main edge-detection workflow is mostly local. <br>
Mitigation: Review before install and prefer a cleaned build that removes unused helper modules or documents them; do not rely on bundled hardcoded credentials. <br>
Risk: Place-resolution helpers can make third-party geocoding requests and write cache data under the user's home directory. <br>
Mitigation: Avoid invoking place-resolution helpers unless third-party geocoding requests and home-directory cache writes are acceptable for the deployment. <br>


## Reference(s): <br>
- [Artifact README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Canny Sample Output Manifest](artifact/_test_canny/output-manifest.json) <br>
- [Sobel Sample Output Manifest](artifact/_test_sobel/output-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown instructions with CLI commands; generated runs produce GeoTIFF, GeoJSON, and JSON manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally for synthetic and local raster workflows; optional place-resolution helpers may use network geocoding and local cache writes.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact CHANGELOG and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
