## Description: <br>
Segments raster imagery into object instances with threshold or Otsu foreground separation, connected-component labeling, and per-instance attribute extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to turn local or synthetic GeoTIFF imagery into instance-level vector and raster outputs for inspection, QA, or downstream GIS workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the shipped package includes network, downloader, cache, and credential-reading modules beyond the local segmentation command. <br>
Mitigation: Treat installation as a review install and remove or disable the geocoding, downloader, cache, and credential modules unless those capabilities are intentionally needed. <br>
Risk: The main CLI is locally scoped, but the broader bundled code is not fully disclosed in the user-facing documentation. <br>
Mitigation: Review the bundled modules and restrict execution to trusted inputs and environments before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-instance-segmentation) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Code, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON, GeoTIFF, JSON manifest, and command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instances.geojson, instance_labels.tif, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
