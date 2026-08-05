## Description: <br>
Maps mangrove distribution and multi-date change by fusing NDVI, NDWI coastline distance, coastal-buffer rules, and optional SAR tidal signatures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and coastal-monitoring teams use this skill to generate mangrove masks, fusion-score rasters, area statistics, and gain/loss change outputs from synthetic scenes or user-provided multiband GeoTIFF imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security scan marked the release suspicious because the package includes under-disclosed credential, geocoding, download, and cache code outside the documented offline raster-processing purpose. <br>
Mitigation: Review the package before installation and prefer a release where those helpers are removed or clearly gated. <br>
Risk: The server security guidance reports a hardcoded Earthdata credential in the shipped package. <br>
Mitigation: Use a version with the embedded credential removed and rotated before deployment. <br>
Risk: The documented offline behavior may not cover all bundled helper code paths. <br>
Mitigation: Run the skill in a network-restricted environment unless the relevant helper behavior has been reviewed and explicitly allowed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-mangrove-mapping) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands, Configuration instructions] <br>
**Output Format:** [GeoTIFF rasters, JSON statistics/manifests, and CLI text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include mangrove masks, score rasters, optional change rasters, area statistics, and a run manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
