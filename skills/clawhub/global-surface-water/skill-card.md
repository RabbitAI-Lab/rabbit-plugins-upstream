## Description: <br>
Download JRC Global Surface Water data layers including occurrence, change, seasonality, recurrence, transition, and extent from Landsat-derived 30m surface-water data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial workflows use this skill to download JRC Global Surface Water GeoTIFF layers for a bounding box or resolved place and inspect available layers or dataset metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the optional place-name lookup can send sensitive place names or areas of interest to geocoding services and cache them locally. <br>
Mitigation: Prefer explicit --bbox coordinates for sensitive work, avoid --place for confidential locations, and clear ~/.geoskill_core_cache after use. <br>
Risk: Dependency or installation choices can affect the security posture of a local download workflow. <br>
Mitigation: Install with reviewed and pinned dependency versions before using the skill in managed environments. <br>


## Reference(s): <br>
- [JRC Global Surface Water Explorer](https://global-surface-water.appspot.com/) <br>
- [Google Earth Engine Dataset: JRC/GSW1_4/GlobalSurfaceWater](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater) <br>
- [Pekel et al. 2016, Nature](https://doi.org/10.1038/nature20584) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; downloaded GeoTIFF files and optional JSON QA summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the requested layer, bbox or place, dataset version, and tile coverage.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
