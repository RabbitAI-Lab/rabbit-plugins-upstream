## Description: <br>
Maps sea ice type and concentration from SAR sigma0 imagery using dB-scale Otsu thresholding, GLCM texture refinement, and sliding-window concentration analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing teams use this skill to classify open water, young ice, and multi-year ice from local SAR sigma0 GeoTIFFs or synthetic test scenes, then generate concentration rasters and area statistics for sea-ice analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports under-disclosed shared helper modules for third-party geocoding, downloads, broad credential handling, and hardcoded Earthdata credentials. <br>
Mitigation: Review before installing, remove or clearly disclose unused shared helpers, eliminate hardcoded credentials, and avoid sensitive environments until those issues are addressed. <br>
Risk: Dependencies are not pinned in the artifact. <br>
Mitigation: Pin and review dependencies before deployment, then run the package in a controlled local environment. <br>
Risk: The scanner verdict is suspicious despite the main SAR mapping workflow being local and coherent. <br>
Mitigation: Treat the release as requiring manual security review before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-sea-ice-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python CLI commands and generated GeoTIFF, JSON, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ice_type.tif, ice_concentration.tif, ice_statistics.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
