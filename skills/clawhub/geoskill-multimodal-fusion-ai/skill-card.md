## Description: <br>
Normalizes multi-source raster inputs, fuses them with automatic or user-specified weights, and produces fused raster and joint classification outputs using an offline NumPy workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial engineers, and remote-sensing practitioners use this skill to combine local multi-band raster modalities, test synthetic fusion scenarios, and generate fused GeoTIFF, classification, report, and manifest files for downstream GIS workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security scan flags undisclosed auxiliary capabilities for network access, downloads, credential-store reads, and home-directory persistence alongside the advertised offline raster-fusion workflow. <br>
Mitigation: Review the bundled helper modules before installation, remove or disable unused network/download/credential helpers when deploying, and run the skill in a constrained environment with only the files and network access it needs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-multimodal-fusion-ai) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON reports, console status text, and command-line usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces fused.tif, classification.tif, fusion_report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
