## Description: <br>
Generates cloud-free satellite image composites and cloud coverage statistics using multi-temporal median or percentile compositing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to process multi-temporal satellite rasters or synthetic offline scenes into cloud-free composites, cloud coverage statistics, and processing manifests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include credential, geocoding, download, and home-directory cache capabilities that are broader than the advertised local cloud-removal entrypoint. <br>
Mitigation: Review the package before installation and remove or disable unrelated helper modules when only local compositing is needed. <br>
Risk: The security evidence reports hardcoded Earthdata fallback credentials in bundled helpers. <br>
Mitigation: Rotate exposed credentials before publishing or use, and prefer environment-managed credentials in isolated runtime environments. <br>
Risk: Remote geocoding and generic download helpers may introduce network access outside the core offline workflow. <br>
Mitigation: Run the skill in synthetic or local-input mode in a network-restricted environment unless those bundled capabilities are explicitly required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cloud-removal-gapfilling) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, files] <br>
**Output Format:** [Python CLI guidance plus GeoTIFF and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces cloud_free_composite.tif, cloud_stats.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
