## Description: <br>
Maps agricultural frost risk from daily minimum temperature rasters and DEM data using terrain correction, frost-frequency statistics, frost-date metrics, and GeoTIFF/JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
GIS, climate, and agricultural-risk practitioners use this skill to run local frost-risk mapping over a bounding box or supplied temperature and DEM rasters. It supports offline synthetic validation and produces frost risk, frost-free-period, frost-frequency, and summary-statistics outputs for downstream review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network and credential helper modules, including a hardcoded Earthdata username/password. <br>
Mitigation: Review before installation, remove or rotate hardcoded credentials, and disclose or remove unused network and credential helpers. <br>
Risk: Dependency versions are not pinned, which can change runtime behavior across environments. <br>
Mitigation: Pin and review dependencies before deployment in shared or production environments. <br>
Risk: Vendored provenance needs correction before the package can be treated as low-risk. <br>
Mitigation: Fix or document vendored provenance and re-run security review before broad deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-frost-risk-mapping) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON statistics/manifests, and concise command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include frost_risk.tif, frost_free_period.tif, frost_frequency.tif, frost_stats.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
