## Description: <br>
Fits pixel-wise linear or exponential trends across multi-period impervious surface fraction data, calculates growth rates, and identifies growth hotspots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to analyze local or synthetic impervious-surface time series and produce growth-rate rasters, hotspot masks, and run manifests for downstream review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vendored credential-handling code includes an embedded Earthdata account credential. <br>
Mitigation: Remove embedded credential defaults and require credentials through environment variables, .netrc, or user-managed secret files before installation. <br>
Risk: Vendored geocoding and download helpers can perform network requests and cache data, even though the main trend tool can run locally. <br>
Mitigation: Review or remove unused network helpers, document any network and cache behavior, and use synthetic or local-input mode when offline processing is required. <br>
Risk: Runtime dependencies are not pinned in requirements.txt. <br>
Mitigation: Pin and review numpy, rasterio, and scipy versions before use in sensitive or reproducible environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-impervious-surface-trend) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Configuration] <br>
**Output Format:** [GeoTIFF rasters, JSON manifest/statistics, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces trend_slope.tif, hotspots.tif, growth_statistics.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
