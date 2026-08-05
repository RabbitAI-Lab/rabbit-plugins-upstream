## Description: <br>
Multi-directional hillshade with vertical exaggeration and color overlay using the Horn algorithm. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to generate shaded-relief visualizations from local DEM GeoTIFF data or synthetic offline terrain. It supports multi-directional weighted compositing, vertical exaggeration, and terrain color overlays for terrain inspection and presentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled modules include under-disclosed web geocoding, downloader, credential lookup, and caching behavior beyond the documented local hillshade entrypoint. <br>
Mitigation: Review or remove unused bundled modules before installation, and document any optional network or cache behavior that remains. <br>
Risk: Security evidence reports a plaintext Earthdata password in bundled credential code. <br>
Mitigation: Remove the credential, rotate the exposed password, and require users to provide secrets through environment variables or local secret files. <br>
Risk: Dependencies are listed without pinned versions. <br>
Mitigation: Pin and review dependency versions before deployment in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-hillshade-visualization) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [CLI guidance plus generated PNG, GeoTIFF, JSON metadata, and JSON run manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs are color_shaded.png, hillshade.tif, hillshade_meta.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
