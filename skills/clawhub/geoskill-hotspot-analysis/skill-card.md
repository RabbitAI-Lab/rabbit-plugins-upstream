## Description: <br>
Identifies statistically significant hotspots and coldspots using Getis-Ord Gi*, Gaussian kernel density estimation, and multi-scale significance testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS analysts use this skill to run local hotspot and coldspot analysis over synthetic data or local GeoTIFF inputs and produce geospatial analysis artifacts for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes bundled geocoding, download, and credential-handling modules beyond the documented local hotspot-analysis path. <br>
Mitigation: Review the package before installation, run it in an isolated environment, and remove or disable unused helper modules before operational use. <br>
Risk: Security guidance identifies embedded Earthdata credentials as requiring action. <br>
Mitigation: Remove or rotate the embedded Earthdata credentials and rely on user-managed secrets or environment variables. <br>
Risk: Unpinned Python dependencies can change behavior or supply-chain exposure over time. <br>
Mitigation: Pin dependency versions before operational use and scan the resolved environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-hotspot-analysis) <br>
- [README](artifact/README.md) <br>
- [CHANGELOG](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance for running a Python CLI that writes GeoTIFF rasters, JSON statistics, and a JSON output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary files include gi_star_zscore.tif, hotspot_significance.tif, kernel_density.tif, hotspot_stats.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
