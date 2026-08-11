## Description: <br>
Maps relative species richness and habitat quality from NDVI productivity, NDVI texture, and terrain heterogeneity proxies, producing GeoTIFF and JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and conservation teams use this skill to estimate biodiversity proxy maps for protected-area siting, ecological baseline surveys, and biodiversity conservation priority screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network, downloader, cache, and credential helpers alongside the documented local raster workflow. <br>
Mitigation: Review those helper modules before installation or execution, and test the skill in an isolated environment. <br>
Risk: Security evidence reports an exposed Earthdata password in the package. <br>
Mitigation: Remove the credential from the release, rotate the exposed password, and avoid invoking credential helpers until a cleaned release is available. <br>
Risk: Dependencies are not version-pinned, which can change runtime behavior across installations. <br>
Mitigation: Pin and review dependencies before using the skill in a managed or production environment. <br>


## Reference(s): <br>
- [Skill README](README.md) <br>
- [Skill Instructions](SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-biodiversity-mapping) <br>
- [Publisher Profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF files, JSON parameter and manifest files, and concise CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local raster-processing outputs, including species_richness.tif, habitat_quality.tif, richness_params.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
