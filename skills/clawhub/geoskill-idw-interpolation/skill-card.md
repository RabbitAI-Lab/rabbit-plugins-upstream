## Description: <br>
Performs Inverse Distance Weighting (IDW) spatial interpolation with configurable power and search settings, producing an interpolated raster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial engineers use this skill to run local IDW interpolation over a WGS84 bounding box or local input data and generate raster results with a run manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include network, downloader, cache, and credential-handling capabilities beyond the advertised offline IDW workflow. <br>
Mitigation: Review or remove unrelated helper modules before deployment, run the skill in a restricted environment, and avoid exposing credentials unless those capabilities are explicitly needed. <br>
Risk: Server-side security evidence marks the release as suspicious because the bundled capabilities do not match the stated offline purpose. <br>
Mitigation: Install only from a trusted publisher, scan the package before use, and require human review before commercial deployment. <br>
Risk: Generated raster manifests may omit fields such as resolution or nodata in some runs. <br>
Mitigation: Validate raster metadata and downstream assumptions before using outputs in production geospatial analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-idw-interpolation) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [Text or Markdown guidance for running the CLI; generated artifacts include a GeoTIFF raster and JSON run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary file outputs are idw_result.tif and output-manifest.json; synthetic mode can run with locally generated data.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
