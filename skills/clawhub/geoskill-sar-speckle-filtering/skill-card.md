## Description: <br>
Applies Lee, Frost, and multilook speckle filtering to single- or multi-band SAR intensity GeoTIFFs, with optional synthetic SAR scene generation, and writes filtered raster outputs plus parameter metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to reduce speckle noise in SAR intensity imagery while preserving useful edges and texture. It supports local GeoTIFF inputs and a synthetic offline mode for testing workflows without external data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence rates the release as suspicious because bundled helper modules include credential, geocoding, download, and home-directory cache capabilities that are broader than the documented offline SAR filtering task. <br>
Mitigation: Review the package before installation, run it in an isolated environment, and remove or disable unrelated bundled modules if only local SAR filtering is needed. <br>
Risk: The documented main workflow is local, but bundled capabilities could make network requests or interact with user credentials if invoked. <br>
Mitigation: Restrict execution to the documented entrypoint and local or synthetic inputs, and block network access when validating offline use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-speckle-filtering) <br>
- [README.md](README.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands] <br>
**Output Format:** [GeoTIFF raster files, JSON manifests or parameter files, and concise console messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces filtered.tif, filter_params.json, and output-manifest.json under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
